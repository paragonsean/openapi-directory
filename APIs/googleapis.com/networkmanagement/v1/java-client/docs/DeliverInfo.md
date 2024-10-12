

# DeliverInfo

Details of the final state \"deliver\" and associated resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipAddress** | **String** | IP address of the target (if applicable). |  [optional] |
|**resourceUri** | **String** | URI of the resource that the packet is delivered to. |  [optional] |
|**target** | [**TargetEnum**](#TargetEnum) | Target type where the packet is delivered to. |  [optional] |



## Enum: TargetEnum

| Name | Value |
|---- | -----|
| TARGET_UNSPECIFIED | &quot;TARGET_UNSPECIFIED&quot; |
| INSTANCE | &quot;INSTANCE&quot; |
| INTERNET | &quot;INTERNET&quot; |
| GOOGLE_API | &quot;GOOGLE_API&quot; |
| GKE_MASTER | &quot;GKE_MASTER&quot; |
| CLOUD_SQL_INSTANCE | &quot;CLOUD_SQL_INSTANCE&quot; |
| PSC_PUBLISHED_SERVICE | &quot;PSC_PUBLISHED_SERVICE&quot; |
| PSC_GOOGLE_API | &quot;PSC_GOOGLE_API&quot; |
| PSC_VPC_SC | &quot;PSC_VPC_SC&quot; |
| SERVERLESS_NEG | &quot;SERVERLESS_NEG&quot; |
| STORAGE_BUCKET | &quot;STORAGE_BUCKET&quot; |
| PRIVATE_NETWORK | &quot;PRIVATE_NETWORK&quot; |
| CLOUD_FUNCTION | &quot;CLOUD_FUNCTION&quot; |
| APP_ENGINE_VERSION | &quot;APP_ENGINE_VERSION&quot; |
| CLOUD_RUN_REVISION | &quot;CLOUD_RUN_REVISION&quot; |



