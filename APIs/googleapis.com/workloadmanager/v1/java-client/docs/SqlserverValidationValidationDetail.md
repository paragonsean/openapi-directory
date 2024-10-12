

# SqlserverValidationValidationDetail

Message describing the Sqlserver validation metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | [**List&lt;SqlserverValidationDetails&gt;**](SqlserverValidationDetails.md) | Required. Details wraps map that represents collected data names and values. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. The Sqlserver system that the validation data is from. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SQLSERVER_VALIDATION_TYPE_UNSPECIFIED | &quot;SQLSERVER_VALIDATION_TYPE_UNSPECIFIED&quot; |
| OS | &quot;OS&quot; |
| DB_LOG_DISK_SEPARATION | &quot;DB_LOG_DISK_SEPARATION&quot; |
| DB_MAX_PARALLELISM | &quot;DB_MAX_PARALLELISM&quot; |
| DB_CXPACKET_WAITS | &quot;DB_CXPACKET_WAITS&quot; |
| DB_TRANSACTION_LOG_HANDLING | &quot;DB_TRANSACTION_LOG_HANDLING&quot; |
| DB_VIRTUAL_LOG_FILE_COUNT | &quot;DB_VIRTUAL_LOG_FILE_COUNT&quot; |
| DB_BUFFER_POOL_EXTENSION | &quot;DB_BUFFER_POOL_EXTENSION&quot; |
| DB_MAX_SERVER_MEMORY | &quot;DB_MAX_SERVER_MEMORY&quot; |
| INSTANCE_METRICS | &quot;INSTANCE_METRICS&quot; |
| DB_INDEX_FRAGMENTATION | &quot;DB_INDEX_FRAGMENTATION&quot; |
| DB_TABLE_INDEX_COMPRESSION | &quot;DB_TABLE_INDEX_COMPRESSION&quot; |
| DB_BACKUP_POLICY | &quot;DB_BACKUP_POLICY&quot; |



