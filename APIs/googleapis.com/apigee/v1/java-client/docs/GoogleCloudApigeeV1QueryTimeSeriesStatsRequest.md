

# GoogleCloudApigeeV1QueryTimeSeriesStatsRequest

QueryTimeSeriesStatsRequest represents a query that returns a collection of time series sequences grouped by their values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | **List&lt;String&gt;** | List of dimension names to group the aggregations by. If no dimensions are passed, a single trend line representing the requested metric aggregations grouped by environment is returned. |  [optional] |
|**filter** | **String** | Filter further on specific dimension values. Follows the same grammar as custom report&#39;s filter expressions. Example, apiproxy eq &#39;foobar&#39;. https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters |  [optional] |
|**metrics** | [**List&lt;GoogleCloudApigeeV1MetricAggregation&gt;**](GoogleCloudApigeeV1MetricAggregation.md) | Required. List of metrics and their aggregations. |  [optional] |
|**pageSize** | **Integer** | Page size represents the number of time series sequences, one per unique set of dimensions and their values. |  [optional] |
|**pageToken** | **String** | Page token stands for a specific collection of time series sequences. |  [optional] |
|**timeRange** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  |  [optional] |
|**timestampOrder** | [**TimestampOrderEnum**](#TimestampOrderEnum) | Order the sequences in increasing or decreasing order of timestamps. Default is descending order of timestamps (latest first). |  [optional] |
|**windowSize** | [**WindowSizeEnum**](#WindowSizeEnum) | Time buckets to group the stats by. |  [optional] |



## Enum: TimestampOrderEnum

| Name | Value |
|---- | -----|
| ORDER_UNSPECIFIED | &quot;ORDER_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |



## Enum: WindowSizeEnum

| Name | Value |
|---- | -----|
| WINDOW_SIZE_UNSPECIFIED | &quot;WINDOW_SIZE_UNSPECIFIED&quot; |
| MINUTE | &quot;MINUTE&quot; |
| HOUR | &quot;HOUR&quot; |
| DAY | &quot;DAY&quot; |
| MONTH | &quot;MONTH&quot; |



