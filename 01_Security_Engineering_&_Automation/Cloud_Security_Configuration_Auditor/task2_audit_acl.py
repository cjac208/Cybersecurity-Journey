# task2_audit_acl.py
import boto3
from moto import mock_aws

@mock_aws
def audit_acls():
    s3 = boto3.client("s3", region_name="us-east-1")

    # Initialize mock bucket with public ACL permissions
    s3.create_bucket(Bucket="public-marketing-assets")
    s3.put_bucket_acl(Bucket="public-marketing-assets", ACL="public-read")

    # Evaluate Access Control List configurations for universal exposure
    acl = s3.get_bucket_acl(Bucket="public-marketing-assets")
    for grant in acl.get("Grants", []):
        grantee = grant.get("Grantee", {})
        if grantee.get("Type") == "Group" and "AllUsers" in grantee.get("URI", ""):
            print("[EXPOSED] public-marketing-assets has a public ACL!")

if __name__ == "__main__":
    audit_acls()