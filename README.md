# SOC Automation Home Lab

## 📖Project Overview: 
This project simulates a real-world Security Operations Center (SOC) environment. The goal was to build an automated incident response pipeline that detects malicious activity, triggers alerts, and automates the initial triage and enrichment process, drastically reducing "mean time to respond" (MTTR).

## 🛠️ Tools & Technologies
* **Virtualization:** Vultr (Cloud Infrastructure), VirtualBox (Endpoint Simulation)
* **Detection & SIEM:** Wazuh 
* **Incident Response:** TheHive5 
* **SOAR Automation:** Shuffle
* **Telemetry:** Sysmon, Mimikatz

## 🚀 Key Features
* **End-to-End Pipeline:** Automated ingestion of endpoint logs from Windows 10 via Wazuh to a centralized SOC dashboard.
* **Threat Detection:** Configured Sysmon to capture adversarial behaviors, specifically using Mimikatz to simulate credential dumping.
* **SOAR Integration:** Utilized Shuffle.io to create automated workflows that:
  * Ingest alerts via Wazuh Webhook URI.
  * Automatically enrich alerts with hash reputation checks.
  * Open and categorize incident cases in TheHive.
  * Send automated notification alerts to the SOC team.

## 🏗️ Architecture(Optional: Insert a simple flow diagram here. You can use a tool like draw.io or Excalidraw to show: Windows Endpoint -> Wazuh -> Shuffle -> TheHive)

## 🖼️ Project Gallery(Replace these placeholders with your actual screenshots)
Shuffle Workflow: [Add image] — The logic behind the automated triage.
Wazuh Dashboard: [Add image] — Visualizing detected Mimikatz execution.
TheHive Case Management: [Add image] — The resulting automated ticket in TheHive.

## 💡 Lessons Learned 
* **Persistence & Automation:** Tackled the challenges of database persistence in Docker-based SOC stacks, learning to manage service dependencies (depends_on and healthchecks) to ensure data integrity across reboots. 
* **System Hardening & Security:** Navigated the balance between endpoint security (Windows Defender) and the need to run red-team tools for testing and verification.
