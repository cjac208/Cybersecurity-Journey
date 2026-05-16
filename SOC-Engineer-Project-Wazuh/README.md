# Advanced Malware Analysis & Payload De-obfuscation
**Environment:** Browser-Based Memory Sandbox (CyberChef)
**Status:** Planned
**Role Simulated:** SOC Analyst / Incident Responder

---

## Project Goal
To analyze, decode, and extract Indicators of Compromise (IOCs) from a heavily obfuscated PowerShell script discovered on a corporate workstation.

## Tools & Analytics Used
* **Analysis Platform:** CyberChef (GCHQ Utility).
* **Operations Used:** From Base64, Decode Text, Regular Expressions (Regex), Defang URL.
* **Skills Demonstrated:** Reverse engineering fundamentals, malware triage, alert analysis.

## 📈 Analysis Methodology
1. **Ingestion:** Captured the raw, encrypted malicious string from the simulated workstation log.
2. **Layer 1 Decoding (Base64):** Applied a 'From Base64' recipe to convert the scrambled text back into legible ASCII string payloads.
3. **Layer 2 Parsing (Defanging):** Identified a malicious hidden destination URL. Applied a defanging operation to make the link unclickable and safe for documentation.

## 🛡️ Technical Evidence & Verification
### 1. Raw Malicious Input
![Raw Obfuscated Input String](assets/cyberchef_input.png)
*Description: The initial encrypted payload string as found in the security alerts.*

### 2. Applied CyberChef Recipe Pipeline
![CyberChef Base64 Decode Recipe](assets/cyberchef_recipe.png)
*Description: Building the analytical pipeline to extract the plain-text script data.*

### 3. Decoded Output & Extracted IP/URL
![Decoded Malware Payload Output](assets/cyberchef_output.png)
*Description: The successfully defanged command-and-control destination address.*

---
*Disclaimer: This analysis is performed strictly on static string data inside an isolated memory sandbox and contains zero active malware or risk to host systems.*

