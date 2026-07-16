import pandas as pd
import os

# Constants
EMAIL_DOC = 'YOUR_CSV_PATH_HERE'

def main():
  if not os.path.exists(EMAIL_DOC):
    print("Alert: Email review document is missing or does not exist")
    return

  df = pd.read_csv(EMAIL_DOC)

  # Filter dataframe to isolate entries awaiting analyst disposition;
  # prevents re-processing already categorized threats.
  to_review = df[df['Status'] == "Flagged Manually"]

  if to_review.empty:
    print("No emails to review")
    return

  # Iterate through the queue to facilitate manual analyst verification,
  # transforming raw flags into actionable security data.
  for index, row in to_review.iterrows():
    print(f"\nTarget: {row['Target']}")
    decision = input("Assign email status(M for Malicous/C for clean): ").strip().lower()

    if decision == 'm':
      df.at[index, 'Status'] = 'Malicious'
    elif decision == 'c':
      df.at[index, 'Status'] = 'Clean'
    else:
      print("Skipping email for further review")
  
  # Persist changes back to the CSV; index=False maintains a clean 
  # schema without creating duplicate index columns in the source file.
  df.to_csv(EMAIL_DOC, index=False)
  print("Email review document updated")
  return

if __name__ == "__main__":
  main()
