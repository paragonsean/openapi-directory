# MicrosoftStorageSync.ServerEndpointSyncSessionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filesNotSyncingErrors** | [**[ServerEndpointFilesNotSyncingError]**](ServerEndpointFilesNotSyncingError.md) | Array of per-item errors coming from the last sync session. | [optional] [readonly] 
**lastSyncPerItemErrorCount** | **Number** | Last sync per item error count. | [optional] [readonly] 
**lastSyncResult** | **Number** | Last sync result (HResult) | [optional] [readonly] 
**lastSyncSuccessTimestamp** | **Date** | Last sync success timestamp | [optional] [readonly] 
**lastSyncTimestamp** | **Date** | Last sync timestamp | [optional] [readonly] 
**persistentFilesNotSyncingCount** | **Number** | Count of persistent files not syncing. | [optional] [readonly] 
**transientFilesNotSyncingCount** | **Number** | Count of transient files not syncing. | [optional] [readonly] 


