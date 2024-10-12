

# ConfigManagementSyncState

State indicating an ACM's progress syncing configurations to a cluster

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Sync status code |  [optional] |
|**errors** | [**List&lt;ConfigManagementSyncError&gt;**](ConfigManagementSyncError.md) | A list of errors resulting from problematic configs. This list will be truncated after 100 errors, although it is unlikely for that many errors to simultaneously exist. |  [optional] |
|**importToken** | **String** | Token indicating the state of the importer. |  [optional] |
|**lastSync** | **String** | Deprecated: use last_sync_time instead. Timestamp of when ACM last successfully synced the repo The time format is specified in https://golang.org/pkg/time/#Time.String |  [optional] |
|**lastSyncTime** | **String** | Timestamp type of when ACM last successfully synced the repo |  [optional] |
|**sourceToken** | **String** | Token indicating the state of the repo. |  [optional] |
|**syncToken** | **String** | Token indicating the state of the syncer. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| SYNC_CODE_UNSPECIFIED | &quot;SYNC_CODE_UNSPECIFIED&quot; |
| SYNCED | &quot;SYNCED&quot; |
| PENDING | &quot;PENDING&quot; |
| ERROR | &quot;ERROR&quot; |
| NOT_CONFIGURED | &quot;NOT_CONFIGURED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| UNAUTHORIZED | &quot;UNAUTHORIZED&quot; |
| UNREACHABLE | &quot;UNREACHABLE&quot; |



