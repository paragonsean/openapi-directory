

# AggregateRequest

Next id: 10

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateBy** | [**List&lt;AggregateBy&gt;**](AggregateBy.md) | The specification of data to be aggregated. At least one aggregateBy spec must be provided. All data that is specified will be aggregated using the same bucketing criteria. There will be one dataset in the response for every aggregateBy spec. |  [optional] |
|**bucketByActivitySegment** | [**BucketByActivity**](BucketByActivity.md) |  |  [optional] |
|**bucketByActivityType** | [**BucketByActivity**](BucketByActivity.md) |  |  [optional] |
|**bucketBySession** | [**BucketBySession**](BucketBySession.md) |  |  [optional] |
|**bucketByTime** | [**BucketByTime**](BucketByTime.md) |  |  [optional] |
|**endTimeMillis** | **String** | The end of a window of time. Data that intersects with this time window will be aggregated. The time is in milliseconds since epoch, inclusive. The maximum allowed difference between start_time_millis // and end_time_millis is 7776000000 (roughly 90 days). |  [optional] |
|**filteredDataQualityStandard** | [**List&lt;FilteredDataQualityStandardEnum&gt;**](#List&lt;FilteredDataQualityStandardEnum&gt;) | DO NOT POPULATE THIS FIELD. It is ignored. |  [optional] |
|**startTimeMillis** | **String** | The start of a window of time. Data that intersects with this time window will be aggregated. The time is in milliseconds since epoch, inclusive. |  [optional] |



## Enum: List&lt;FilteredDataQualityStandardEnum&gt;

| Name | Value |
|---- | -----|
| DATA_QUALITY_UNKNOWN | &quot;dataQualityUnknown&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_ESH2002 | &quot;dataQualityBloodPressureEsh2002&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_ESH2010 | &quot;dataQualityBloodPressureEsh2010&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_AAMI | &quot;dataQualityBloodPressureAami&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_AA | &quot;dataQualityBloodPressureBhsAA&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_AB | &quot;dataQualityBloodPressureBhsAB&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_BA | &quot;dataQualityBloodPressureBhsBA&quot; |
| DATA_QUALITY_BLOOD_PRESSURE_BHS_BB | &quot;dataQualityBloodPressureBhsBB&quot; |
| DATA_QUALITY_BLOOD_GLUCOSE_ISO151972003 | &quot;dataQualityBloodGlucoseIso151972003&quot; |
| DATA_QUALITY_BLOOD_GLUCOSE_ISO151972013 | &quot;dataQualityBloodGlucoseIso151972013&quot; |



