# SOC Automation Home Lab: Automated Threat Detection & Enrichment

### 📖Project Overview: 
This project demonstrates an automated security monitoring and alert enrichment pipeline. By simulating malicious activity on a Windows 10 endpoint, the system automatically detects threats via Wazuh, orchestrates log enrichment through Shuffle, and centralizes incident reporting within TheHive.

The goal of this lab was to streamline the "Detection-to-Report" lifecycle, reducing manual analyst work by automating the gathering of threat intelligence and initial incident categorization.

### 🛠️ Tools & Technologies
* **Virtualization:** Vultr (Cloud Infrastructure), VirtualBox (Endpoint Isolation)
* **Endpoint Monitoring:** Windows 10, Sysmon, Mimikatz (Telemetry Generation)
* **Detection:** Wazuh (SIEM/XDR)
* **Orchestration:** Shuffle (SOAR)
* **Case Management:** TheHive (Incident Response)
* **Threat Intelligence:** VirusTotal API

### ⚙️ Key Features
(Insert your diagram here—if you don't have one, keep it simple with text:)
[Windows 10 / Sysmon] → [Wazuh Agent] → [Wazuh Server] → [Shuffle Webhook] → [VirusTotal API] → [TheHive API]

### 🚀 Key Features
* **Automated Telemetry Generation:** Utilized Mimikatz to trigger specific Windows Event IDs, verified via Sysmon to ensure high-fidelity detection.
* **Automated Enrichment Pipeline:** When Wazuh detects a security event, a Shuffle workflow is triggered via Webhook. It automatically parses the alert, queries VirusTotal for hash reputation, and formats the metadata.
* **Streamlined Alert Reporting:** Instead of manual triage, alerts are pushed directly into TheHive, fully enriched with threat intelligence, allowing analysts to immediately assess the severity.
  
### 📋 Methodology
* **Infrastructure:** Deployed Linux instances on Vultr for centralized logging and case management.
* **Telemetry:** Installed Sysmon on a Windows 10 VM to capture process execution, file integrity, and network connection events.
* **Detection Logic:** Configured Wazuh to monitor specific Sysmon Event IDs (e.g., process creation for mimikatz.exe).
* **Orchestration:** Built a custom Shuffle workflow to act as the "middleman," transforming raw logs into actionable incident reports.

### 💡 Lessons Learned 
* **Persistence & Automation:** Tackled the challenges of database persistence in Docker-based SOC stacks, learning to manage service dependencies (depends_on and healthchecks) to ensure data integrity across reboots. 
* **System Hardening & Security:** Navigated the balance between endpoint security (Windows Defender) and the need to run red-team tools for testing and verification.

### Return page

[Return to Repository Hub](https://github.com/RobNor12/RobNor12/blob/overview/README.md)
