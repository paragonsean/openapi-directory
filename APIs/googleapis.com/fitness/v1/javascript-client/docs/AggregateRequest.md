# FitnessApi.AggregateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregateBy** | [**[AggregateBy]**](AggregateBy.md) | The specification of data to be aggregated. At least one aggregateBy spec must be provided. All data that is specified will be aggregated using the same bucketing criteria. There will be one dataset in the response for every aggregateBy spec. | [optional] 
**bucketByActivitySegment** | [**BucketByActivity**](BucketByActivity.md) |  | [optional] 
**bucketByActivityType** | [**BucketByActivity**](BucketByActivity.md) |  | [optional] 
**bucketBySession** | [**BucketBySession**](BucketBySession.md) |  | [optional] 
**bucketByTime** | [**BucketByTime**](BucketByTime.md) |  | [optional] 
**endTimeMillis** | **String** | The end of a window of time. Data that intersects with this time window will be aggregated. The time is in milliseconds since epoch, inclusive. The maximum allowed difference between start_time_millis // and end_time_millis is 7776000000 (roughly 90 days). | [optional] 
**filteredDataQualityStandard** | **[String]** | DO NOT POPULATE THIS FIELD. It is ignored. | [optional] 
**startTimeMillis** | **String** | The start of a window of time. Data that intersects with this time window will be aggregated. The time is in milliseconds since epoch, inclusive. | [optional] 



## Enum: [FilteredDataQualityStandardEnum]


* `dataQualityUnknown` (value: `"dataQualityUnknown"`)

* `dataQualityBloodPressureEsh2002` (value: `"dataQualityBloodPressureEsh2002"`)

* `dataQualityBloodPressureEsh2010` (value: `"dataQualityBloodPressureEsh2010"`)

* `dataQualityBloodPressureAami` (value: `"dataQualityBloodPressureAami"`)

* `dataQualityBloodPressureBhsAA` (value: `"dataQualityBloodPressureBhsAA"`)

* `dataQualityBloodPressureBhsAB` (value: `"dataQualityBloodPressureBhsAB"`)

* `dataQualityBloodPressureBhsBA` (value: `"dataQualityBloodPressureBhsBA"`)

* `dataQualityBloodPressureBhsBB` (value: `"dataQualityBloodPressureBhsBB"`)

* `dataQualityBloodGlucoseIso151972003` (value: `"dataQualityBloodGlucoseIso151972003"`)

* `dataQualityBloodGlucoseIso151972013` (value: `"dataQualityBloodGlucoseIso151972013"`)




