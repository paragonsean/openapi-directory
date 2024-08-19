# GoogleAnalyticsDataApi.RunPivotReportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregates** | [**[Row]**](Row.md) | Aggregation of metric values. Can be totals, minimums, or maximums. The returned aggregations are controlled by the metric_aggregations in the pivot. The type of aggregation returned in each row is shown by the dimension_values which are set to \&quot;RESERVED_\&quot;. | [optional] 
**dimensionHeaders** | [**[DimensionHeader]**](DimensionHeader.md) | Describes dimension columns. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows. | [optional] 
**kind** | **String** | Identifies what kind of resource this message is. This &#x60;kind&#x60; is always the fixed string \&quot;analyticsData#runPivotReport\&quot;. Useful to distinguish between response types in JSON. | [optional] 
**metadata** | [**ResponseMetaData**](ResponseMetaData.md) |  | [optional] 
**metricHeaders** | [**[MetricHeader]**](MetricHeader.md) | Describes metric columns. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows. | [optional] 
**pivotHeaders** | [**[PivotHeader]**](PivotHeader.md) | Summarizes the columns and rows created by a pivot. Each pivot in the request produces one header in the response. If we have a request like this: \&quot;pivots\&quot;: [{ \&quot;fieldNames\&quot;: [\&quot;country\&quot;, \&quot;city\&quot;] }, { \&quot;fieldNames\&quot;: \&quot;eventName\&quot; }] We will have the following &#x60;pivotHeaders&#x60; in the response: \&quot;pivotHeaders\&quot; : [{ \&quot;dimensionHeaders\&quot;: [{ \&quot;dimensionValues\&quot;: [ { \&quot;value\&quot;: \&quot;United Kingdom\&quot; }, { \&quot;value\&quot;: \&quot;London\&quot; } ] }, { \&quot;dimensionValues\&quot;: [ { \&quot;value\&quot;: \&quot;Japan\&quot; }, { \&quot;value\&quot;: \&quot;Osaka\&quot; } ] }] }, { \&quot;dimensionHeaders\&quot;: [{ \&quot;dimensionValues\&quot;: [{ \&quot;value\&quot;: \&quot;session_start\&quot; }] }, { \&quot;dimensionValues\&quot;: [{ \&quot;value\&quot;: \&quot;scroll\&quot; }] }] }] | [optional] 
**propertyQuota** | [**PropertyQuota**](PropertyQuota.md) |  | [optional] 
**rows** | [**[Row]**](Row.md) | Rows of dimension value combinations and metric values in the report. | [optional] 


