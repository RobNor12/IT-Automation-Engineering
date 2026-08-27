# Hybrid Active Directory Lab: Windows 11 Enterprise & Ubuntu Integration

A multi-OS enterprise lab environment featuring a cloud-hosted Windows Server Domain Controller (`RNORRIS-LAB.LOCAL`), a native Windows 11 Enterprise client, and an Ubuntu Linux client integrated via Samba, Winbind, and PAM.

### 🏗️ Architecture & Topology

- **Domain Controller (DC):** Windows Server (`cwm3382.rnorris-lab.local`)
  - **IP Address:** `104.225.141.208`
  - **Domain Name:** `RNORRIS-LAB.LOCAL` (NetBIOS: `LAB`)
- **Client 1:** Windows 11 Enterprise (`WIN-CLIENT01`) (Natively joined via Active Directory domain join)
- **Client 2:** Ubuntu Linux (`rnorris-ubuntu`) (Integrated via Samba/Winbind & PAM)

### 🛠️ Key Technical Challenges & Solutions

### Ubuntu Linux Client Integration 

Integrating Linux clients with an Active Directory domain introduces notorious cross-platform friction. Below are the primary infrastructure hurdles and solutions implemented in this lab:

### 1. DNS Resolution & `systemd-resolved` Routing
- **The Challenge:** Ubuntu’s local resolver (`127.0.0.53`) failed to resolve internal `.local` Active Directory SRV records (`_ldap._tcp.dc._msdcs.RNORRIS-LAB.LOCAL`), causing domain join authentication dropouts (*"No logon servers are currently available"*).
- **The Solution:** Explicitly forced network interface DNS routing to point directly to the cloud Domain Controller and bound the domain search suffix:
  ```bash
  sudo resolvectl dns <INTERFACE_NAME> 104.225.141.208
  sudo resolvectl domain <INTERFACE_NAME> ~rnorris-lab.local
  ```

### 🖥️ Windows 11 Enterprise Client Integration

Unlike the Linux client, the Windows 11 Enterprise endpoint was provisioned using the native operating system workflow:

1. **Domain Join:** Configured the system properties (`sysdm.cpl`) to join the `RNORRIS-LAB.LOCAL` domain using administrative credentials.
2. **DNS Validation:** Verified network adapter IPv4 settings pointed correctly to the cloud Domain Controller (`104.225.141.208`).
3. **Authentication Check:** Validated successful domain sign-in and remote management connectivity back to `cwm3382`.

