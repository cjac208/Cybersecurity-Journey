# task3_audit_policy.py
import boto3
import json
from moto import mock_aws

@mock_aws
def audit_policies():
    s3 = boto3.client("s3", region_name="us-east-1")

    # Initialize mock bucket with an anonymous wildcard access policy
    s3.create_bucket(Bucket="exposed-developer-backups")
    public_policy = '{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Principal": "*", "Action":  "s3:GetObject"}]}'
    s3.put_bucket_policy(Bucket="exposed-developer-backups", Policy=public_policy)

    #Parse resource-based policy JSON payload to detect risky conifgurations
    response = s3.get_bucket_policy(Bucket="exposed-developer-backups")
    policy_dict = json.loads(response["Policy"])
    for stmt in policy_dict.get("Statement", []):
        if stmt.get("Effect") == "Allow" and stmt.get("Principal") == "*":
            print("[EXPOSED] exposed-developer-backups has a public Policy!")

if __name__ == "__main__":
    audit_policies()