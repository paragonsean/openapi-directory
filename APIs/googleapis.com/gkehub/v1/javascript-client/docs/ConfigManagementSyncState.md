# GkeHubApi.ConfigManagementSyncState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Sync status code | [optional] 
**errors** | [**[ConfigManagementSyncError]**](ConfigManagementSyncError.md) | A list of errors resulting from problematic configs. This list will be truncated after 100 errors, although it is unlikely for that many errors to simultaneously exist. | [optional] 
**importToken** | **String** | Token indicating the state of the importer. | [optional] 
**lastSync** | **String** | Deprecated: use last_sync_time instead. Timestamp of when ACM last successfully synced the repo The time format is specified in https://golang.org/pkg/time/#Time.String | [optional] 
**lastSyncTime** | **String** | Timestamp type of when ACM last successfully synced the repo | [optional] 
**sourceToken** | **String** | Token indicating the state of the repo. | [optional] 
**syncToken** | **String** | Token indicating the state of the syncer. | [optional] 



## Enum: CodeEnum


* `SYNC_CODE_UNSPECIFIED` (value: `"SYNC_CODE_UNSPECIFIED"`)

* `SYNCED` (value: `"SYNCED"`)

* `PENDING` (value: `"PENDING"`)

* `ERROR` (value: `"ERROR"`)

* `NOT_CONFIGURED` (value: `"NOT_CONFIGURED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `UNAUTHORIZED` (value: `"UNAUTHORIZED"`)

* `UNREACHABLE` (value: `"UNREACHABLE"`)




