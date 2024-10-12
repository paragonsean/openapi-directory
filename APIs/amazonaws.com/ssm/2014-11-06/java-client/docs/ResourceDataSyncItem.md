

# ResourceDataSyncItem

Information about a resource data sync configuration, including its current status and last successful sync.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncName** | [**String**](String.md) |  |  [optional] |
|**syncType** | [**String**](String.md) |  |  [optional] |
|**syncSource** | [**ResourceDataSyncItemSyncSource**](ResourceDataSyncItemSyncSource.md) |  |  [optional] |
|**s3Destination** | [**ResourceDataSyncItemS3Destination**](ResourceDataSyncItemS3Destination.md) |  |  [optional] |
|**lastSyncTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastSuccessfulSyncTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**syncLastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastStatus** | [**LastResourceDataSyncStatus**](LastResourceDataSyncStatus.md) |  |  [optional] |
|**syncCreatedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastSyncStatusMessage** | [**String**](String.md) |  |  [optional] |



