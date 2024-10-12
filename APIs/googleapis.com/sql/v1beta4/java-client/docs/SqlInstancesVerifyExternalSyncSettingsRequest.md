

# SqlInstancesVerifyExternalSyncSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mysqlSyncConfig** | [**MySqlSyncConfig**](MySqlSyncConfig.md) |  |  [optional] |
|**syncMode** | [**SyncModeEnum**](#SyncModeEnum) | External sync mode |  [optional] |
|**verifyConnectionOnly** | **Boolean** | Flag to enable verifying connection only |  [optional] |
|**verifyReplicationOnly** | **Boolean** | Optional. Flag to verify settings required by replication setup only |  [optional] |



## Enum: SyncModeEnum

| Name | Value |
|---- | -----|
| EXTERNAL_SYNC_MODE_UNSPECIFIED | &quot;EXTERNAL_SYNC_MODE_UNSPECIFIED&quot; |
| ONLINE | &quot;ONLINE&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



