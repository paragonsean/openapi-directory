# WorkloadManagerApi.SqlserverValidationValidationDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**[SqlserverValidationDetails]**](SqlserverValidationDetails.md) | Required. Details wraps map that represents collected data names and values. | [optional] 
**type** | **String** | Optional. The Sqlserver system that the validation data is from. | [optional] 



## Enum: TypeEnum


* `SQLSERVER_VALIDATION_TYPE_UNSPECIFIED` (value: `"SQLSERVER_VALIDATION_TYPE_UNSPECIFIED"`)

* `OS` (value: `"OS"`)

* `DB_LOG_DISK_SEPARATION` (value: `"DB_LOG_DISK_SEPARATION"`)

* `DB_MAX_PARALLELISM` (value: `"DB_MAX_PARALLELISM"`)

* `DB_CXPACKET_WAITS` (value: `"DB_CXPACKET_WAITS"`)

* `DB_TRANSACTION_LOG_HANDLING` (value: `"DB_TRANSACTION_LOG_HANDLING"`)

* `DB_VIRTUAL_LOG_FILE_COUNT` (value: `"DB_VIRTUAL_LOG_FILE_COUNT"`)

* `DB_BUFFER_POOL_EXTENSION` (value: `"DB_BUFFER_POOL_EXTENSION"`)

* `DB_MAX_SERVER_MEMORY` (value: `"DB_MAX_SERVER_MEMORY"`)

* `INSTANCE_METRICS` (value: `"INSTANCE_METRICS"`)

* `DB_INDEX_FRAGMENTATION` (value: `"DB_INDEX_FRAGMENTATION"`)

* `DB_TABLE_INDEX_COMPRESSION` (value: `"DB_TABLE_INDEX_COMPRESSION"`)

* `DB_BACKUP_POLICY` (value: `"DB_BACKUP_POLICY"`)




