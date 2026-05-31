import re
import json
import os

#Define local file system paths
LOG_FILE = "01_Security_Engineering_&_Automation/Automated_Log_Parser/access.log"
MOCK_JSON = "01_Security_Engineering_&_Automation/Automated_Log_Parser/mock_threat_data.json"
REPORT_FILE = "01_Security_Engineering_&_Automation/Automated_Log_Parser/threat_report.txt"

# Regex pattern to extract IP address and detect malicious payloads
# Looks for common indicators like etc/passwd or SQL injection (UNION SELECT)
LOG_PATTERN = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(?:/etc/passwd|UNION\s+SELECT)'

print("[*] Initializing Security Parser...")

# Load the threat intelligence JSON database
try:
    with open(MOCK_JSON,'r') as json_file:
        threat_intel = json.load(json_file)
except FileNotFoundError:
    print(f"[!] Error: {MOCK_JSON} not found. please check your path.")
    exit(1)

# Read the access log and parse malicious entries
flagged_alerts = []

if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as log_file:
            for line in log_file:
                 match = re.search(LOG_PATTERN, line, re.IGNORECASE)
                 if match:
                     ip = match.group('ip')  

                     # Look up the IP in the mock threat data (default to 0 if not found)
                     malicious_score = threat_intel.get(ip, {}).get ("malicious", 0)

                     # Append structured data for the report
                     flagged_alerts.append({
                         "ip": ip,
                         "score": malicious_score,
                         "raw_line": line.strip()
                     })
else:
     print(f"[!] Error: {LOG_FILE} not found.")
     exit(1)

# Generate the Permanent Threat Report Text File
print(f"[*] Writing security alerts to {REPORT_FILE}...")
with open(REPORT_FILE, "w") as report:
     report.write("==================================================\n")
     report.write("         AUTOMATED THREAT INTELLIGENCE REPORT     \n")
     report.write("==================================================\n")
     report.write(f"Generated Alerts Count: {len(flagged_alerts)}\n\n")

     for alert in flagged_alerts:
         report.write(f"ALERT: Malicious Traffic Detected\n")
         report.write(f"Attackign IP: {alert['ip']}\n")
         report.write(f"Threat Intel Malicious Score: {alert['score']}/100\n")
         report.write(f"Triggered Log Line: {alert['raw_line']}\n")
         report.write("-"* 50 + "\n")

print("[+] Success! 'threat_report.txt' has been generated perfectly.")