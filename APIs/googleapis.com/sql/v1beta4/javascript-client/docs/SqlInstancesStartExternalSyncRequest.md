# CloudSqlAdminApi.SqlInstancesStartExternalSyncRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysqlSyncConfig** | [**MySqlSyncConfig**](MySqlSyncConfig.md) |  | [optional] 
**skipVerification** | **Boolean** | Whether to skip the verification step (VESS). | [optional] 
**syncMode** | **String** | External sync mode. | [optional] 
**syncParallelLevel** | **String** | Optional. Parallel level for initial data sync. Currently only applicable for MySQL. | [optional] 



## Enum: SyncModeEnum


* `EXTERNAL_SYNC_MODE_UNSPECIFIED` (value: `"EXTERNAL_SYNC_MODE_UNSPECIFIED"`)

* `ONLINE` (value: `"ONLINE"`)

* `OFFLINE` (value: `"OFFLINE"`)





## Enum: SyncParallelLevelEnum


* `EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED` (value: `"EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED"`)

* `MIN` (value: `"MIN"`)

* `OPTIMAL` (value: `"OPTIMAL"`)

* `MAX` (value: `"MAX"`)




