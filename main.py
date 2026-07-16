import os
import pandas as pd
import requests

# Constants
VT_DOMAIN_URL = 'https://virustotal.com'
EMAIL_DOC = 'YOUR_EMAIL_REVIEW_FILE_PATH_HERE'
VT_API_KEY = 'YOUR_API_KEY_FILE_PATH_HERE'

def get_api_key():
    if not os.path.exists(VT_API_KEY):
        print("Security Alert: 'api_key.txt' is missing! Please upload it to the folder.")
        return None
    else:
        # Utilizing pandas to read the key file allows for easy expansion if
        # the key storage format changes to CSV/Table-based config later.
        df = pd.read_csv(VT_API_KEY, header=None)
        api_key = str(df.iloc[0, 0]).strip()
        print("Security Check: Key successfully loaded into memory from external file!")
        return api_key

def validate_api_request(target_input, api_key):
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }

    # Normalizing input: Ensuring the API receives only the domain portion
    # to prevent malformed queries from email-style inputs.
    if "@" in target_input:
        domain = target_input.split("@")[-1]
    else:
        domain = target_input

    api_endpoint = f"{VT_DOMAIN_URL}/{domain}"

    response = requests.get(api_endpoint, headers=headers)

    # Mapping API status codes to custom internal state markers
    if response.status_code == 429:
        print("Security Alert: Rate limit exceeded. Please try again later.")
        return "RATE_LIMIT"
    elif response.status_code == 404:
        print(f"Security Alert: Domain '{domain}' not found in VirusTotal database.")
        return "NOT_FOUND"
    elif response.status_code != 200:
        print(f"Security Alert: API request failed with status code {response.status_code}.")
        return "INVALID"

    data = response.json()

    try:
        # Deep-path extraction into nested JSON response structure;
        # KeyError handling prevents crashes if VT changes their response format.
        malicious_count = data['data']['attributes']['last_analysis_stats']['malicious']
        return malicious_count
    except KeyError:
        print("Security Alert: Malicious count data missing from the response payload.")
        return "INVALID"

def is_already_flagged(target):
    # Check if the CSV exists and if the target is already present in the "Target" column
    if os.path.exists(EMAIL_DOC):
        df = pd.read_csv(EMAIL_DOC)
        # Check if target exists
        match = df[df['Target'].str.lower() == target.lower()]
        if not match.empty:
            # Return the status (e.g., "Malicious", "Clean", "Flagged Manually")
            return match.iloc[0]['Status']
    return None

def get_flag_details(target):
    if os.path.exists(EMAIL_DOC):
        df = pd.read_csv(EMAIL_DOC)
        match = df[df['Target'].str.lower() == target.lower()]
        if not match.empty:
            # Returns a dictionary of the latest data
            return {
                "status": match.iloc[0]['Status'],
                "last_updated": match.iloc[0].get('Last_Updated', 'N/A')
            }
    return None

def main():
    api_key = get_api_key()
    if not api_key:
        return

    target = input("Enter email or domain to check: ").strip()
    if not target:
        return

    # Check for details
    details = get_flag_details(target)
    if details:
        print(f"[!] Info: '{target}' found in audit logs.")
        print(f"    Status: {details['status']}")
        print(f"    Last Verified: {details['last_updated']}")
        return

    # Capture the actual status returned from the CSV
    status = is_already_flagged(target)

    if status:
        # Give the user specific info instead of a generic "already reviewed"
        print(f"[!] Info: '{target}' is already in our records with status: '{status}'.")
        return

    malicious_count = validate_api_request(target, api_key)

    if malicious_count == "RATE_LIMIT":
        return
    elif malicious_count == "NOT_FOUND":
        # A 404 in VT context indicates no prior scans; treat as low risk but unverified.
        print("This domain has not been analyzed yet. It is currently clean or unknown.")
        malicious_count = 0
    elif malicious_count == "INVALID":
        print("Could not validate the target due to an unexpected API error.")
        return

    if malicious_count > 0:
        print(f"[-] Alert: {target} has been flagged as MALICIOUS by {malicious_count} engines!")
    else:
        print(f"[+] Clean: {target} has not been flagged as malicious.")
        choice = input("Would you like to manually flag this target for review anyway? (y/n): ").strip().lower()

        # Input sanitization loop to enforce strict 'y/n' interaction flow.
        while choice not in ['y', 'n']:
            print("Invalid choice. Please enter 'y' or 'n'.")
            choice = input("Would you like to flag this target? (y/n): ").strip().lower()

        if choice == 'y':
            log_df = pd.DataFrame([[target, "Flagged Manually"]], columns=["Target", "Status"])

            # Appending mode maintains the audit trail; dynamic header logic
            # prevents header duplication in the persistent review file.
            file_exists = os.path.isfile(EMAIL_DOC)
            log_df.to_csv(EMAIL_DOC, mode='a', header=not file_exists, index=False)
            print(f"Success: {target} has been written to your review sheet.")
        else:
            print("Target not flagged. Have a good day!")

if __name__ == "__main__":
    main()
