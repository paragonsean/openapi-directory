

# MetricsPostBodySchemaParameters

The parameters for a single metrics query

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**List&lt;AggregationEnum&gt;**](#List&lt;AggregationEnum&gt;) | The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used. |  [optional] |
|**filter** | **String** | An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving. |  [optional] |
|**interval** | **String** | The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response. |  [optional] |
|**metricId** | **MetricId** |  |  |
|**orderby** | **String** | The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified. |  [optional] |
|**segment** | [**List&lt;SegmentEnum&gt;**](#List&lt;SegmentEnum&gt;) | The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter. |  [optional] |
|**timespan** | **String** | The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. |  [optional] |
|**top** | **Integer** | The number of segments to return.  This value is only valid when segment is specified. |  [optional] |



## Enum: List&lt;AggregationEnum&gt;

| Name | Value |
|---- | -----|
| MIN | &quot;min&quot; |
| MAX | &quot;max&quot; |
| AVG | &quot;avg&quot; |
| SUM | &quot;sum&quot; |
| COUNT | &quot;count&quot; |
| UNIQUE | &quot;unique&quot; |



## Enum: List&lt;SegmentEnum&gt;

| Name | Value |
|---- | -----|
| APPLICATION_BUILD | &quot;applicationBuild&quot; |
| APPLICATION_VERSION | &quot;applicationVersion&quot; |
| AUTHENTICATED_OR_ANONYMOUS_TRAFFIC | &quot;authenticatedOrAnonymousTraffic&quot; |
| BROWSER | &quot;browser&quot; |
| BROWSER_VERSION | &quot;browserVersion&quot; |
| CITY | &quot;city&quot; |
| CLOUD_ROLE_NAME | &quot;cloudRoleName&quot; |
| CLOUD_SERVICE_NAME | &quot;cloudServiceName&quot; |
| CONTINENT | &quot;continent&quot; |
| COUNTRY_OR_REGION | &quot;countryOrRegion&quot; |
| DEPLOYMENT_ID | &quot;deploymentId&quot; |
| DEPLOYMENT_UNIT | &quot;deploymentUnit&quot; |
| DEVICE_TYPE | &quot;deviceType&quot; |
| ENVIRONMENT | &quot;environment&quot; |
| HOSTING_LOCATION | &quot;hostingLocation&quot; |
| INSTANCE_NAME | &quot;instanceName&quot; |



