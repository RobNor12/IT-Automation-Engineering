# Python Email Threat Parser & Triage System
### Overview
The Python Email Threat Parser & Triage System is a professional-grade automation pipeline designed to streamline the incident response process. By separating automated threat intelligence from manual investigation, this tool allows security analysts to move from rapid identification to documented disposition, significantly reducing manual research time.

### Architecture & Workflow
This project utilizes a Dual-Tool Architecture:

* **main.py** (Threat Intelligence Parser): Automates initial domain/email reputation lookups via the VirusTotal API. It identifies known threats and allows analysts to escalate suspicious targets for further review.

* **reviewer.py** (Investigation Queue): A dedicated triage interface for analysts. This script allows you to review flagged targets, assign a final security disposition (Malicious or Clean), and maintain an audit-ready log for your team.

### Technology Used
* **Python:** Core logic, API integration, and user-flow management.

* **Pandas:** Used for robust CSV data management, maintaining a persistent audit trail, and duplicate prevention.

* **VirusTotal API:** Real-time threat intelligence data acquisition.

### Key Features
* **Automated Intelligence Lookup:** Queries VirusTotal in real-time to retrieve maliciousness statistics.

* **Intelligent Duplicate Prevention:** Checks existing local records before querying the API, saving limited API credits.

* **Workflow-Driven Disposition:** Supports a clear lifecycle for every investigated target: Unknown/Clean → Flagged for Review → Resolved.

* **Audit-Ready Logging:** All investigations are logged in a structured format suitable for security team reporting.

### How to Use
* **1. Setup**
Ensure your api_key.txt file is placed in your project directory (as defined in your constants).

* **2. Threat Parsing (main.py)**
Run the script to check a domain or email address.

      Bash
      python main.py

The script will check the local database for existing reviews.

If new, it queries VirusTotal.

If clean, you can opt to flag it for the review queue.



* **3. Review & Disposition (reviewer.py)**
Use this script to process your queue.

      Bash
      python reviewer.py
  
This will iterate through all entries marked as "Flagged Manually."

Allows the analyst to make the final determination (Malicious vs. Clean) and updates the master CSV file.

### MIT License
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
