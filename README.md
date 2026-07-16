# Python Email Threat Parser & Triage System
### 📖 Overview
The Python Email Threat Parser & Triage System is an automated incident response pipeline designed to move security operations from manual, error-prone tasks to a standardized, audit-ready workflow. This system automates the ingestion of suspicious domains, provides real-time threat intelligence, and enforces strict operational security (OPSEC) for incident disposition.

### ⚙️ Architecture & Workflow
This project implements a secure, two-part pipeline that mirrors enterprise SOAR (Security Orchestration, Automation, and Response) workflows:

* **main.py (Threat Intelligence Parser):** Automates initial reputation lookups via the VirusTotal API. It provides rapid identification and allows analysts to escalate suspicious targets into a centralized review queue.

* **reviewer.py (Secure Triage Interface):** A gated triage environment for security analysts. It ensures that only authorized personnel can finalize incident status, providing full attribution and forensic auditing.

### 🛠 Technology Used
* **Python:** Core logic, API integration, and user-flow management.

* **Pandas:** Used for robust CSV data management, maintaining a persistent audit trail, and duplicate prevention.

* **VirusTotal API:** Real-time threat intelligence data acquisition.

### 🚀 Key Features
* **Identity & Access Management (IAM):** The triage script implements a secure authentication gate, ensuring only authorized analysts can access and modify the threat log.

* **Forensic Audit Logging:** Every disposition (Malicious/Clean) is automatically timestamped and attributed to the specific analyst who performed the review.

* **Schema Resiliency:** The system dynamically manages database growth, ensuring audit columns are initialized and maintained without requiring manual data migration.

* **Operational Discipline:** By moving from manual checks to a scripted workflow, the system eliminates human error, standardizes decision-making, and maintains a clean, searchable incident history.

### ⚙️ How to Use
* **Setup:**

  * Download the requirements.txt folder to ensure you have the Libraries necessary to run these programs

  * Ensure your "api_key.txt" file, "email_review.csv" file, and "authorized_analyst.csv" file are placed securely in your project directory. These files are not included in this repository

* **Threat Parsing (main.py):**

   * Run the script to check a domain or email address.

            Bash
            python main.py
            
   * Performs reputation checks.

   * Duplicates are ignored to conserve API credits.

   * Suspicious targets are queued for the Reviewer.

* **Review & Disposition (reviewer.py):**

  * Use this script to process your queue.

            Bash
            python reviewer.py
  
  * Authenticates the analyst against the known_analyst.csv list.

  * Provides an interactive queue for disposition (M/C).

  * Automatically appends Reviewer ID and Last_Updated timestamp to the audit log.

### MIT License
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
