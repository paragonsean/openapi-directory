# CloudSqlAdminApi.SqlInstancesVerifyExternalSyncSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysqlSyncConfig** | [**MySqlSyncConfig**](MySqlSyncConfig.md) |  | [optional] 
**syncMode** | **String** | External sync mode | [optional] 
**verifyConnectionOnly** | **Boolean** | Flag to enable verifying connection only | [optional] 
**verifyReplicationOnly** | **Boolean** | Optional. Flag to verify settings required by replication setup only | [optional] 



## Enum: SyncModeEnum


* `EXTERNAL_SYNC_MODE_UNSPECIFIED` (value: `"EXTERNAL_SYNC_MODE_UNSPECIFIED"`)

* `ONLINE` (value: `"ONLINE"`)

* `OFFLINE` (value: `"OFFLINE"`)




