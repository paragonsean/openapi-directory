

# SqlInstancesStartExternalSyncRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mysqlSyncConfig** | [**MySqlSyncConfig**](MySqlSyncConfig.md) |  |  [optional] |
|**skipVerification** | **Boolean** | Whether to skip the verification step (VESS). |  [optional] |
|**syncMode** | [**SyncModeEnum**](#SyncModeEnum) | External sync mode. |  [optional] |
|**syncParallelLevel** | [**SyncParallelLevelEnum**](#SyncParallelLevelEnum) | Optional. Parallel level for initial data sync. Currently only applicable for MySQL. |  [optional] |



## Enum: SyncModeEnum

| Name | Value |
|---- | -----|
| EXTERNAL_SYNC_MODE_UNSPECIFIED | &quot;EXTERNAL_SYNC_MODE_UNSPECIFIED&quot; |
| ONLINE | &quot;ONLINE&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



## Enum: SyncParallelLevelEnum

| Name | Value |
|---- | -----|
| EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED | &quot;EXTERNAL_SYNC_PARALLEL_LEVEL_UNSPECIFIED&quot; |
| MIN | &quot;MIN&quot; |
| OPTIMAL | &quot;OPTIMAL&quot; |
| MAX | &quot;MAX&quot; |



