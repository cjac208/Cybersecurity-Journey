# cloud_auditor.py
import boto3
import json
from botocore.exceptions import ClientError
from moto import mock_aws

# ANSI terminal formatting variables for colorized report
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

@mock_aws
def full_audit():
    s3 = boto3.client("s3", region_name="us-east-1")

    # Intilialize full security assessment baseline infrastructure
    s3.create_bucket(Bucket="company-secure-financials")
    s3.create_bucket(Bucket="public-marketing-assets")
    s3.put_bucket_acl(Bucket="public-marketing-assets", ACL="public-read")

    #1. Create a bucket that looks public, but is saved by the Master Switch (BPA)
    s3.create_bucket(Bucket="protected-marketing-backup")
    s3.put_bucket_acl(Bucket="protected-marketing-backup", ACL="public-read")
    s3.put_public_access_block(
        Bucket="protected-marketing-backup",
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True 
        }                                                                  
    )

    buckets = s3.list_buckets().get("Buckets",[])
    print(f"{YELLOW}[*] Orchestrating Accelerated Environment-Wide Audit...{RESET}\n")

    for b in buckets:
        name = b["Name"]
        is_exposed = False
        bpa_enabled = False

        # Check Master Switch: Block Public Access (BPA) Status
        try:
            bpa = s3. get_public_access_block(Bucket=name)
            config = bpa.get("PublicAccessBlockConfiguration", {})
            if config.get("BlockPublicAcls") and config.get("BlockPublicPolicy"):
                bpa_enabled = True
        except ClientError:
            # AWS displays an error if BPA is not configured at all (defaults disabled)
            bpa_enabled = False

        # Check legacy ACL configurations
        acl = s3.get_bucket_acl(Bucket=name)
        for grant in acl.get("Grants", []):
            if "AllUsers" in grant.get("Grantee", {}).get("URI", ""):
                # If the master switch is ON, it blocks the public ACL exposure
                if not bpa_enabled:
                    is_exposed = True
        # Generate colorized compliance status reports
        if is_exposed:
            print(f"{RED}[EXPOSED] Bucket: {name}")
            print(f"          Risk: Public access allowed without Block Public Access guardrails!{RESET}\n")
        elif bpa_enabled and name == "protected-marketing-backup":
            print(f"{GREEN}[SECURE] Bucket: {name}")
            print(f"          Status: Bad ACL overridden by active Black Public Access Master Switch.{RESET}\n")
        else:
            print(f"{GREEN}[SECURE] Bucket: {name}{RESET}\n")

if __name__ == "__main__":
    full_audit()