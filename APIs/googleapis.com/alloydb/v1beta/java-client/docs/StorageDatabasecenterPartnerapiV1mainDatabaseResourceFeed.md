

# StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed

DatabaseResourceFeed is the top level proto to be used to ingest different database resource level events into Condor platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feedTimestamp** | **String** | Required. Timestamp when feed is generated. |  [optional] |
|**feedType** | [**FeedTypeEnum**](#FeedTypeEnum) | Required. Type feed to be ingested into condor |  [optional] |
|**recommendationSignalData** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData.md) |  |  [optional] |
|**resourceHealthSignalData** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData.md) |  |  [optional] |
|**resourceId** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceId**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceId.md) |  |  [optional] |
|**resourceMetadata** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata.md) |  |  [optional] |



## Enum: FeedTypeEnum

| Name | Value |
|---- | -----|
| FEEDTYPE_UNSPECIFIED | &quot;FEEDTYPE_UNSPECIFIED&quot; |
| RESOURCE_METADATA | &quot;RESOURCE_METADATA&quot; |
| OBSERVABILITY_DATA | &quot;OBSERVABILITY_DATA&quot; |
| SECURITY_FINDING_DATA | &quot;SECURITY_FINDING_DATA&quot; |
| RECOMMENDATION_SIGNAL_DATA | &quot;RECOMMENDATION_SIGNAL_DATA&quot; |



