import pulumi

from core.cognito import user_pool, user_pool_client
from core.s3 import admin_app_bucket, data_bucket

pulumi.export("user-pool-id", user_pool.id)
pulumi.export("user-pool-client-id", user_pool_client.id)
pulumi.export("data-bucket", data_bucket.bucket_name)
pulumi.export("admin-app-bucket", admin_app_bucket.bucket_name)
