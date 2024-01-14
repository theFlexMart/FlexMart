import pulumi
from pulumi_aws_native import cognito

org = pulumi.Config("org")  # get config from org namespace
config = pulumi.Config("core-infra")

prefix = f"{org.get('name')}-{config.get('env')}"

# Create a Cognito User Pool of authorized users
user_pool = cognito.UserPool(f"{prefix}-user-pool")
user_pool_client = cognito.UserPoolClient(
    f"{prefix}-user-pool-client",
    user_pool_id=user_pool.id,
    explicit_auth_flows=["ADMIN_NO_SRP_AUTH"],
)
