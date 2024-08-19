

# StorageDatabasecenterPartnerapiV1mainOperationError

An error that occurred during a backup creation operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | Identifies the specific error that occurred. REQUIRED |  [optional] |
|**errorType** | [**ErrorTypeEnum**](#ErrorTypeEnum) |  |  [optional] |
|**message** | **String** | Additional information about the error encountered. REQUIRED |  [optional] |



## Enum: ErrorTypeEnum

| Name | Value |
|---- | -----|
| OPERATION_ERROR_TYPE_UNSPECIFIED | &quot;OPERATION_ERROR_TYPE_UNSPECIFIED&quot; |
| KMS_KEY_ERROR | &quot;KMS_KEY_ERROR&quot; |
| DATABASE_ERROR | &quot;DATABASE_ERROR&quot; |
| STOCKOUT_ERROR | &quot;STOCKOUT_ERROR&quot; |
| CANCELLATION_ERROR | &quot;CANCELLATION_ERROR&quot; |
| SQLSERVER_ERROR | &quot;SQLSERVER_ERROR&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |



