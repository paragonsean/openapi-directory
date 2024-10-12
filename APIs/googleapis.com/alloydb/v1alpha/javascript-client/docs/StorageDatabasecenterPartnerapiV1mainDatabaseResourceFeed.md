# AlloyDbApi.StorageDatabasecenterPartnerapiV1mainDatabaseResourceFeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedTimestamp** | **String** | Required. Timestamp when feed is generated. | [optional] 
**feedType** | **String** | Required. Type feed to be ingested into condor | [optional] 
**recommendationSignalData** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceRecommendationSignalData.md) |  | [optional] 
**resourceHealthSignalData** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData.md) |  | [optional] 
**resourceId** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceId**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceId.md) |  | [optional] 
**resourceMetadata** | [**StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata**](StorageDatabasecenterPartnerapiV1mainDatabaseResourceMetadata.md) |  | [optional] 



## Enum: FeedTypeEnum


* `FEEDTYPE_UNSPECIFIED` (value: `"FEEDTYPE_UNSPECIFIED"`)

* `RESOURCE_METADATA` (value: `"RESOURCE_METADATA"`)

* `OBSERVABILITY_DATA` (value: `"OBSERVABILITY_DATA"`)

* `SECURITY_FINDING_DATA` (value: `"SECURITY_FINDING_DATA"`)

* `RECOMMENDATION_SIGNAL_DATA` (value: `"RECOMMENDATION_SIGNAL_DATA"`)




