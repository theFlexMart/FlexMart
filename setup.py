import pulumi

from core.cognito import user_pool, user_pool_client
from core.dynamodb import data_table

pulumi.export("user-pool-id", user_pool.id)
pulumi.export("user-pool-client-id", user_pool_client.id)
pulumi.export("data-table", data_table.name)
