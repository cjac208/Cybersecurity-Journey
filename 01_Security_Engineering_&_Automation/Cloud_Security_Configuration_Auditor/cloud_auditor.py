# cloud_auditor.py
import boto3
import json
from moto import mock_aws

# ANSI terminal formatting variables for colorized report
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

@mock_aws
def full_audit():
    s3 = boto3.client("s3", region_name="us-east-1")

    # Intilialize full security assessment baseline infrastructure
    s3.create_bucket(Bucket="company-secure-financials")
    s3.create_bucket(Bucket="public-marketing-assets")
    s3.put_bucket_acl(Bucket="public-marketing-assets", ACL="public-read")

    # Orchestrate environment-wide scanner across all identified buckets
    buckets = s3.list_buckets().get("Buckets", [])
    for b in buckets:
        name = b["Name"]
        is_exposed = False

        # Analyze ACL tracking criteria
        acl = s3.get_bucket_acl(Bucket=name)
        for grant in acl.get("Grants", []):
            if "AllUsers" in grant.get("Grantee", {}).get("URI", ""):
                is_exposed = True

        # Generate final structured execution logs
        if is_exposed:
            print(f"{RED}[EXPOSED] Bucket: {name}{RESET}")
        else:
            print(f"{GREEN}[SECURE] Bucket: {name}{RESET}")

if __name__ == "__main__":
    full_audit()