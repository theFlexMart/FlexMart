import pulumi
from pulumi_aws import dynamodb

org = pulumi.Config("org")  # get config from org namespace
config = pulumi.Config("core-infra")

prefix = f"{org.get('name')}-{config.get('env')}"

data_table = dynamodb.Table(
    f"{prefix}-data-table",
    attributes=[
        dynamodb.TableAttributeArgs(name="PK", type="S"),
        dynamodb.TableAttributeArgs(name="SK", type="S"),
    ],
    hash_key="PK",
    range_key="SK",
    billing_mode="PAY_PER_REQUEST",
)
