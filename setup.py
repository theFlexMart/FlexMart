import pulumi

from core.cognito import user_pool, user_pool_client

pulumi.export("user-pool-id", user_pool.id)
pulumi.export("user-pool-client-id", user_pool_client.id)
