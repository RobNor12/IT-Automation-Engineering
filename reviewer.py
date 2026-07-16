import pandas as pd
import os
import datetime

# Constants
EMAIL_DOC = 'YOUR_EMAIL_REVIEW_DOC_PATH_HERE'
AUTH_FILE = 'YOUR_ANALYST_NAME_LIST_PATH_HERE'

def authenticate_analyst():
    if not os.path.exists(AUTH_FILE):
        print("Security Alert: Authorization file missing.")
        return None

    auth_df = pd.read_csv(AUTH_FILE)
    authorized_users = auth_df['analyst_name'].str.lower().tolist()

    user = input("Enter your Analyst ID: ").strip().lower()

    # Identity verification gate: Ensures only authorized personnel 
    # can modify incident disposition logs.
    if user in authorized_users:
        print(f"Access Granted: Welcome, {user}.")
        return user
    else:
        print("ERROR: Unknown analyst, ending program.")
        return None

def main():
    current_analyst = authenticate_analyst()
    if not current_analyst:
        return

    if not os.path.exists(EMAIL_DOC):
        print("Alert: Email review document is missing.")
        return

    df = pd.read_csv(EMAIL_DOC)

    # Schema evolution: Dynamically ensures audit columns exist 
    # for forensic tracking if they were not previously initialized.
    if 'Reviewer' not in df.columns: df['Reviewer'] = ""
    if 'Last_Updated' not in df.columns: df['Last_Updated'] = ""

    # Filter for items requiring analyst disposition to prevent 
    # redundant processing of previously resolved threats.
    to_review = df[df['Status'] == "Flagged Manually"]

    if to_review.empty:
        print("No emails to review")
        return

    for index, row in to_review.iterrows():
        print(f"\nTarget: {row['Target']}")
        decision = input("Assign email status(M for Malicous/C for clean): ").strip().lower()

        if decision in ['m', 'c']:
            # Log disposition, attribute to current analyst, and apply 
            # UTC/local timestamp for immutable audit trail.
            df.at[index, 'Status'] = 'Malicious' if decision == 'm' else 'Clean'
            df.at[index, 'Reviewer'] = current_analyst
            df.at[index, 'Last_Updated'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            print("Skipping...")

    df.to_csv(EMAIL_DOC, index=False)
    print("Email review document updated with audit logs.")

if __name__ == "__main__":
    main()
