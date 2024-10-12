# MicrosoftStorageSync.ServerEndpointSyncStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combinedHealth** | [**HealthState**](HealthState.md) |  | [optional] 
**downloadActivity** | [**SyncActivityStatus**](SyncActivityStatus.md) |  | [optional] 
**downloadHealth** | [**HealthState**](HealthState.md) |  | [optional] 
**downloadStatus** | [**SyncSessionStatus**](SyncSessionStatus.md) |  | [optional] 
**lastUpdatedTimestamp** | **Date** | Last Updated Timestamp | [optional] [readonly] 
**offlineDataTransferStatus** | [**OfflineDataTransferState**](OfflineDataTransferState.md) |  | [optional] 
**syncActivity** | [**SyncActivityState**](SyncActivityState.md) |  | [optional] 
**totalPersistentFilesNotSyncingCount** | **Number** | Total count of persistent files not syncing (combined upload + download). Reserved for future use. | [optional] [readonly] 
**uploadActivity** | [**SyncActivityStatus**](SyncActivityStatus.md) |  | [optional] 
**uploadHealth** | [**HealthState**](HealthState.md) |  | [optional] 
**uploadStatus** | [**SyncSessionStatus**](SyncSessionStatus.md) |  | [optional] 


