#setup_infra.py
import boto3
from moto import mock_aws

@mock_aws
def create_mock_environment():
    # Connect directly to the in-memory mock S3 service
    s3 = boto3.client("s3", region_name="us-east-1")

    # 1. Create a secure private bucket
    s3.create_bucket(Bucket="company-secure-financials")
    
    # 2. Create a bucket simulated as a public via ACL configuration
    s3.create_bucket(Bucket="public-marketing-assets")
    s3.put_bucket_acl(Bucket="public-marketing-assets", ACL="public-read")

    # 3. Create a bucket simulated as public via wide-open Bucket Policy
    s3.create_bucket(Bucket="exposed-developer-backups")
    public_policy = """{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicRead",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::exposed-developer-backups/*"
            }
        ]
    }"""
    s3.put_bucket_policy(Bucket="exposed-developer-backups", Policy=public_policy)

    print("Offline Moto Test Environnment Verified.")

    # Query API to verify visibility of the simulated infrastructure
    response = s3.list_buckets()
    print("--- Discovered Buckets ---")
    for bucket in response.get("Buckets", []):
        print(f"Found Target: {bucket['Name']}")

if __name__ == "__main__":
    create_mock_environment()