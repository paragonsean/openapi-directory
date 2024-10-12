

# DatabaseResourceFeed

DatabaseResourceFeed is the top level proto to be used to ingest different database resource level events into Condor platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feedTimestamp** | **String** | Required. Timestamp when feed is generated. |  [optional] |
|**feedType** | [**FeedTypeEnum**](#FeedTypeEnum) | Required. Type feed to be ingested into condor |  [optional] |
|**recommendationSignalData** | [**DatabaseResourceRecommendationSignalData**](DatabaseResourceRecommendationSignalData.md) |  |  [optional] |
|**resourceHealthSignalData** | [**DatabaseResourceHealthSignalData**](DatabaseResourceHealthSignalData.md) |  |  [optional] |
|**resourceId** | [**DatabaseResourceId**](DatabaseResourceId.md) |  |  [optional] |
|**resourceMetadata** | [**DatabaseResourceMetadata**](DatabaseResourceMetadata.md) |  |  [optional] |



## Enum: FeedTypeEnum

| Name | Value |
|---- | -----|
| FEEDTYPE_UNSPECIFIED | &quot;FEEDTYPE_UNSPECIFIED&quot; |
| RESOURCE_METADATA | &quot;RESOURCE_METADATA&quot; |
| OBSERVABILITY_DATA | &quot;OBSERVABILITY_DATA&quot; |
| SECURITY_FINDING_DATA | &quot;SECURITY_FINDING_DATA&quot; |
| RECOMMENDATION_SIGNAL_DATA | &quot;RECOMMENDATION_SIGNAL_DATA&quot; |



