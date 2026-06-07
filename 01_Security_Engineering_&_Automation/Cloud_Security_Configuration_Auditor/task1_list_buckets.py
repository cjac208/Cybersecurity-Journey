import boto3
from moto import mock_aws

@mock_aws
def list_all_buckets():
    s3 = boto3.client("s3", region_name="us-east-1")

    # Initialize mock target resources
    s3.create_bucket(Bucket="company-secure-financials")
    s3.create_bucket(Bucket="public-marketing-assets")

    # Execute API Discovery loop against the target endpoint
    response = s3.list_buckets()
    bucket_list = response.get("Buckets", [])

    print("--- Discovered Buckets ---")
    for bucket in bucket_list:
        print(f"Found Target: {bucket['Name']}")

if __name__ == "__main__":
    list_all_buckets()
    