

# ConnectorCollectionInfo

Collection and ingestion information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ConnectorCollectionErrorInfo**](ConnectorCollectionErrorInfo.md) |  |  [optional] |
|**lastChecked** | **OffsetDateTime** | Last time the data acquisition process initiated connecting to the external provider |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** | Last time the external data was updated into Azure |  [optional] [readonly] |
|**sourceLastUpdated** | **OffsetDateTime** | Source timestamp of external data currently available in Azure (eg AWS last processed CUR file timestamp) |  [optional] [readonly] |



