import json

# Open threat mock intelligence for read access
with open("01_Security_Engineering_&_Automation/Automated_Log_Parser/mock_threat_data.json", "r") as file:
    # Load JSON data into python dictionary object
    threat_data = json.load(file)

# Define the specific bad IP address that needs to be investigated
target_ip = "185.220.101.5"

# Navigate the layers step-by-step and find the score
# Threat intelligence -> observed_ips -> the bad IP -> reputation_scores -> malicious
malicious_score = threat_data["threat_intelligence"]["observed_ips"][target_ip]["reputation_scores"]["malicious"]

print(malicious_score)
