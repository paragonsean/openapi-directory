# ApigeeApi.GoogleCloudApigeeV1QueryTimeSeriesStatsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | **[String]** | List of dimension names to group the aggregations by. If no dimensions are passed, a single trend line representing the requested metric aggregations grouped by environment is returned. | [optional] 
**filter** | **String** | Filter further on specific dimension values. Follows the same grammar as custom report&#39;s filter expressions. Example, apiproxy eq &#39;foobar&#39;. https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters | [optional] 
**metrics** | [**[GoogleCloudApigeeV1MetricAggregation]**](GoogleCloudApigeeV1MetricAggregation.md) | Required. List of metrics and their aggregations. | [optional] 
**pageSize** | **Number** | Page size represents the number of time series sequences, one per unique set of dimensions and their values. | [optional] 
**pageToken** | **String** | Page token stands for a specific collection of time series sequences. | [optional] 
**timeRange** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  | [optional] 
**timestampOrder** | **String** | Order the sequences in increasing or decreasing order of timestamps. Default is descending order of timestamps (latest first). | [optional] 
**windowSize** | **String** | Time buckets to group the stats by. | [optional] 



## Enum: TimestampOrderEnum


* `ORDER_UNSPECIFIED` (value: `"ORDER_UNSPECIFIED"`)

* `ASCENDING` (value: `"ASCENDING"`)

* `DESCENDING` (value: `"DESCENDING"`)





## Enum: WindowSizeEnum


* `WINDOW_SIZE_UNSPECIFIED` (value: `"WINDOW_SIZE_UNSPECIFIED"`)

* `MINUTE` (value: `"MINUTE"`)

* `HOUR` (value: `"HOUR"`)

* `DAY` (value: `"DAY"`)

* `MONTH` (value: `"MONTH"`)




