# MicrosoftStorageSync.ServerEndpointSyncStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combinedHealth** | [**ServerEndpointSyncHealthState**](ServerEndpointSyncHealthState.md) |  | [optional] 
**downloadActivity** | [**ServerEndpointSyncActivityStatus**](ServerEndpointSyncActivityStatus.md) |  | [optional] 
**downloadHealth** | [**ServerEndpointSyncHealthState**](ServerEndpointSyncHealthState.md) |  | [optional] 
**downloadStatus** | [**ServerEndpointSyncSessionStatus**](ServerEndpointSyncSessionStatus.md) |  | [optional] 
**lastUpdatedTimestamp** | **Date** | Last Updated Timestamp | [optional] [readonly] 
**offlineDataTransferStatus** | [**ServerEndpointOfflineDataTransferState**](ServerEndpointOfflineDataTransferState.md) |  | [optional] 
**syncActivity** | [**ServerEndpointSyncActivityState**](ServerEndpointSyncActivityState.md) |  | [optional] 
**totalPersistentFilesNotSyncingCount** | **Number** | Total count of persistent files not syncing (combined upload + download). | [optional] [readonly] 
**uploadActivity** | [**ServerEndpointSyncActivityStatus**](ServerEndpointSyncActivityStatus.md) |  | [optional] 
**uploadHealth** | [**ServerEndpointSyncHealthState**](ServerEndpointSyncHealthState.md) |  | [optional] 
**uploadStatus** | [**ServerEndpointSyncSessionStatus**](ServerEndpointSyncSessionStatus.md) |  | [optional] 


