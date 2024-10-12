

# ServerEndpointSyncStatus

Server Endpoint sync status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**combinedHealth** | **ServerEndpointSyncHealthState** |  |  [optional] |
|**downloadActivity** | [**ServerEndpointSyncActivityStatus**](ServerEndpointSyncActivityStatus.md) |  |  [optional] |
|**downloadHealth** | **ServerEndpointSyncHealthState** |  |  [optional] |
|**downloadStatus** | [**ServerEndpointSyncSessionStatus**](ServerEndpointSyncSessionStatus.md) |  |  [optional] |
|**lastUpdatedTimestamp** | **OffsetDateTime** | Last Updated Timestamp |  [optional] [readonly] |
|**offlineDataTransferStatus** | **ServerEndpointOfflineDataTransferState** |  |  [optional] |
|**syncActivity** | **ServerEndpointSyncActivityState** |  |  [optional] |
|**totalPersistentFilesNotSyncingCount** | **Long** | Total count of persistent files not syncing (combined upload + download). |  [optional] [readonly] |
|**uploadActivity** | [**ServerEndpointSyncActivityStatus**](ServerEndpointSyncActivityStatus.md) |  |  [optional] |
|**uploadHealth** | **ServerEndpointSyncHealthState** |  |  [optional] |
|**uploadStatus** | [**ServerEndpointSyncSessionStatus**](ServerEndpointSyncSessionStatus.md) |  |  [optional] |



