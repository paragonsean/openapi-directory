

# CreateJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | [**CreateJobRequestDetails**](CreateJobRequestDetails.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of job to be created. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMPORT_ASSETS_FROM_S3 | &quot;IMPORT_ASSETS_FROM_S3&quot; |
| IMPORT_ASSET_FROM_SIGNED_URL | &quot;IMPORT_ASSET_FROM_SIGNED_URL&quot; |
| EXPORT_ASSETS_TO_S3 | &quot;EXPORT_ASSETS_TO_S3&quot; |
| EXPORT_ASSET_TO_SIGNED_URL | &quot;EXPORT_ASSET_TO_SIGNED_URL&quot; |
| EXPORT_REVISIONS_TO_S3 | &quot;EXPORT_REVISIONS_TO_S3&quot; |
| IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES | &quot;IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES&quot; |
| IMPORT_ASSET_FROM_API_GATEWAY_API | &quot;IMPORT_ASSET_FROM_API_GATEWAY_API&quot; |
| CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET | &quot;CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET&quot; |
| IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY | &quot;IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY&quot; |



