# Cloud Security Configuration Auditor

An automated cloud security compliance scnanner engineered in Python utilizing the Boto3 SDK to programmatically identify data exposure risks within Amazon S3 ifnrastructure.

## Technical Overview
To mitigate risks and eliminate overhead costs associated with testing against live cloud infrastructure, this project leverages **Moto** to mock production AWS S3 API endpoints entirely in-memory within a containerized development environment. The tool orchestrates an environment-wide resource discovery loop, parses nested JSON payloads, and evaluates multi-layered identity and access controls.

## Security Controls Evaluated 
* **Access Control Lists (ACLs):** Scans for legacy global grants targeting the 'AllUsers' URI group to detect public visibility.
* **Block Public Access (BPA):** Evaluates the status of the AWS master safety switch to determine if public configurations are actively overidden and blocked by tenant guardrails.

## Directory Structure
```text
Cybersecurity-Journey/
└── 01_Security_Engineering_&_Automation/      
    └── Cloud_Security_Configuration_Auditor/
        ├── cloud_auditor.py          # Integrated compliance scanner
        ├── task1_list_buckets.py      # API discovery loop module
        ├── task2_audit_acl.py        # ACL parsing module
        ├── task3_audit_policy.py     # JSON policy analysis module
        └── README.md                 # Technical documentation
```

## Compliance Output Summary
The script utilizes ANSI terminal escape codes to isolate identified compliance parameters visually:
* **[SECURE]** (Green): Assets Configured with proper private baseline restrictions or explicitly saved by Blocked Public Access overrides.
* **[EXPOSED]** (Red): Critical risk alerts identifying public data exposure without overriding master safety guardrails.