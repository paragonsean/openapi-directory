

# GoogleCloudApigeeV1QueryTabularStatsRequest

Request payload representing the query to be run for fetching security statistics as rows.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | **List&lt;String&gt;** | Required. List of dimension names to group the aggregations by. |  [optional] |
|**filter** | **String** | Filter further on specific dimension values. Follows the same grammar as custom report&#39;s filter expressions. Example, apiproxy eq &#39;foobar&#39;. https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#filters |  [optional] |
|**metrics** | [**List&lt;GoogleCloudApigeeV1MetricAggregation&gt;**](GoogleCloudApigeeV1MetricAggregation.md) | Required. List of metrics and their aggregations. |  [optional] |
|**pageSize** | **Integer** | Page size represents the number of rows. |  [optional] |
|**pageToken** | **String** | Identifies a sequence of rows. |  [optional] |
|**timeRange** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  |  [optional] |



