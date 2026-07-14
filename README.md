# Python Email Threat Parser
### Overview
The Python Email Threat Parser is a security-focused automation tool designed to streamline the triage of suspicious emails and domains. By integrating the VirusTotal API, this script enables security analysts to perform rapid reputation checks on sender domains, automate threat flagging, and maintain an organized research queue for incident response.

### Technology Used
Python: Used for the core script logic, API request handling, and user interaction.

Pandas: Used for robust CSV data management, ensuring persistent storage of flagged threats and efficient duplicate checking.

VirusTotal: The primary threat intelligence source, providing real-time maliciousness statistics for domains and sender addresses.

### Key Features
Automated Intelligence Lookup: Automatically queries the VirusTotal database to retrieve real-time maliciousness data, reducing the need for manual research.

Intelligent Triage Workflow: Normalizes input data (stripping emails to domains) and supports manual flagging for suspicious targets that may not yet be flagged by antivirus engines.

Duplicate Prevention: Includes a local database check to prevent redundant API calls for domains already under review.

Actionable Audit Trail: Automatically logs flagged threats into a structured CSV file, maintaining a clean record for security teams to investigate further.

### How to Use
Prepare your environment: Ensure you have your api_key.txt file ready in your project directory.

Install dependencies: Ensure pandas and requests are installed in your environment.

Run the script:

Bash
python main.py
Enter target: Provide the domain or email address when prompted.

Review results: If the target is flagged, it will notify you immediately; if clean, you can opt to add it to the email_review.csv file for further investigation by your team.

### MIT License
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
