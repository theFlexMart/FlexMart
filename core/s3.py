import pulumi
from pulumi_aws_native import s3

org = pulumi.Config("org")  # get config from org namespace
config = pulumi.Config("core-infra")

prefix = f"{org.get('name')}-{config.get('env')}"

data_bucket = s3.Bucket(f"{prefix}-data-bucket")
admin_app_bucket = s3.Bucket(f"{prefix}-admin-app-bucket")
