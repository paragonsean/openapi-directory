

# ServerEndpointSyncStatus

Server Endpoint sync status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**combinedHealth** | **HealthState** |  |  [optional] |
|**downloadActivity** | [**SyncActivityStatus**](SyncActivityStatus.md) |  |  [optional] |
|**downloadHealth** | **HealthState** |  |  [optional] |
|**downloadStatus** | [**SyncSessionStatus**](SyncSessionStatus.md) |  |  [optional] |
|**lastUpdatedTimestamp** | **OffsetDateTime** | Last Updated Timestamp |  [optional] [readonly] |
|**offlineDataTransferStatus** | **OfflineDataTransferState** |  |  [optional] |
|**syncActivity** | **SyncActivityState** |  |  [optional] |
|**totalPersistentFilesNotSyncingCount** | **Long** | Total count of persistent files not syncing (combined upload + download). Reserved for future use. |  [optional] [readonly] |
|**uploadActivity** | [**SyncActivityStatus**](SyncActivityStatus.md) |  |  [optional] |
|**uploadHealth** | **HealthState** |  |  [optional] |
|**uploadStatus** | [**SyncSessionStatus**](SyncSessionStatus.md) |  |  [optional] |



