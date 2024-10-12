

# GoogleCloudApigeeV1Query


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csvDelimiter** | **String** | Delimiter used in the CSV file, if &#x60;outputFormat&#x60; is set to &#x60;csv&#x60;. Defaults to the &#x60;,&#x60; (comma) character. Supported delimiter characters include comma (&#x60;,&#x60;), pipe (&#x60;|&#x60;), and tab (&#x60;\\t&#x60;). |  [optional] |
|**dimensions** | **List&lt;String&gt;** | A list of dimensions. https://docs.apigee.com/api-platform/analytics/analytics-reference#dimensions |  [optional] |
|**envgroupHostname** | **String** | Hostname needs to be specified if query intends to run at host level. This field is only allowed when query is submitted by CreateHostAsyncQuery where analytics data will be grouped by organization and hostname. |  [optional] |
|**filter** | **String** | Boolean expression that can be used to filter data. Filter expressions can be combined using AND/OR terms and should be fully parenthesized to avoid ambiguity. See Analytics metrics, dimensions, and filters reference https://docs.apigee.com/api-platform/analytics/analytics-reference for more information on the fields available to filter on. For more information on the tokens that you use to build filter expressions, see Filter expression syntax. https://docs.apigee.com/api-platform/analytics/asynch-reports-api#filter-expression-syntax |  [optional] |
|**groupByTimeUnit** | **String** | Time unit used to group the result set. Valid values include: second, minute, hour, day, week, or month. If a query includes groupByTimeUnit, then the result is an aggregation based on the specified time unit and the resultant timestamp does not include milliseconds precision. If a query omits groupByTimeUnit, then the resultant timestamp includes milliseconds precision. |  [optional] |
|**limit** | **Integer** | Maximum number of rows that can be returned in the result. |  [optional] |
|**metrics** | [**List&lt;GoogleCloudApigeeV1QueryMetric&gt;**](GoogleCloudApigeeV1QueryMetric.md) | A list of Metrics. |  [optional] |
|**name** | **String** | Asynchronous Query Name. |  [optional] |
|**outputFormat** | **String** | Valid values include: &#x60;csv&#x60; or &#x60;json&#x60;. Defaults to &#x60;json&#x60;. Note: Configure the delimiter for CSV output using the csvDelimiter property. |  [optional] |
|**reportDefinitionId** | **String** | Asynchronous Report ID. |  [optional] |
|**timeRange** | **Object** | Required. Time range for the query. Can use the following predefined strings to specify the time range: &#x60;last60minutes&#x60; &#x60;last24hours&#x60; &#x60;last7days&#x60; Or, specify the timeRange as a structure describing start and end timestamps in the ISO format: yyyy-mm-ddThh:mm:ssZ. Example: \&quot;timeRange\&quot;: { \&quot;start\&quot;: \&quot;2018-07-29T00:13:00Z\&quot;, \&quot;end\&quot;: \&quot;2018-08-01T00:18:00Z\&quot; } |  [optional] |



