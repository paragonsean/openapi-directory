# GoogleCloudMemorystoreForRedisApi.DatabaseResourceFeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedTimestamp** | **String** | Required. Timestamp when feed is generated. | [optional] 
**feedType** | **String** | Required. Type feed to be ingested into condor | [optional] 
**recommendationSignalData** | [**DatabaseResourceRecommendationSignalData**](DatabaseResourceRecommendationSignalData.md) |  | [optional] 
**resourceHealthSignalData** | [**DatabaseResourceHealthSignalData**](DatabaseResourceHealthSignalData.md) |  | [optional] 
**resourceId** | [**DatabaseResourceId**](DatabaseResourceId.md) |  | [optional] 
**resourceMetadata** | [**DatabaseResourceMetadata**](DatabaseResourceMetadata.md) |  | [optional] 



## Enum: FeedTypeEnum


* `FEEDTYPE_UNSPECIFIED` (value: `"FEEDTYPE_UNSPECIFIED"`)

* `RESOURCE_METADATA` (value: `"RESOURCE_METADATA"`)

* `OBSERVABILITY_DATA` (value: `"OBSERVABILITY_DATA"`)

* `SECURITY_FINDING_DATA` (value: `"SECURITY_FINDING_DATA"`)

* `RECOMMENDATION_SIGNAL_DATA` (value: `"RECOMMENDATION_SIGNAL_DATA"`)




