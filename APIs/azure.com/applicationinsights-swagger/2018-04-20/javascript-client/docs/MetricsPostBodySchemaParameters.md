# ApplicationInsightsDataPlane.MetricsPostBodySchemaParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | **[String]** | The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used. | [optional] 
**filter** | **String** | An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving. | [optional] 
**interval** | **String** | The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response. | [optional] 
**metricId** | [**MetricId**](MetricId.md) |  | 
**orderby** | **String** | The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified. | [optional] 
**segment** | **[String]** | The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter. | [optional] 
**timespan** | **String** | The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. | [optional] 
**top** | **Number** | The number of segments to return.  This value is only valid when segment is specified. | [optional] 



## Enum: [AggregationEnum]


* `min` (value: `"min"`)

* `max` (value: `"max"`)

* `avg` (value: `"avg"`)

* `sum` (value: `"sum"`)

* `count` (value: `"count"`)

* `unique` (value: `"unique"`)





## Enum: [SegmentEnum]


* `applicationBuild` (value: `"applicationBuild"`)

* `applicationVersion` (value: `"applicationVersion"`)

* `authenticatedOrAnonymousTraffic` (value: `"authenticatedOrAnonymousTraffic"`)

* `browser` (value: `"browser"`)

* `browserVersion` (value: `"browserVersion"`)

* `city` (value: `"city"`)

* `cloudRoleName` (value: `"cloudRoleName"`)

* `cloudServiceName` (value: `"cloudServiceName"`)

* `continent` (value: `"continent"`)

* `countryOrRegion` (value: `"countryOrRegion"`)

* `deploymentId` (value: `"deploymentId"`)

* `deploymentUnit` (value: `"deploymentUnit"`)

* `deviceType` (value: `"deviceType"`)

* `environment` (value: `"environment"`)

* `hostingLocation` (value: `"hostingLocation"`)

* `instanceName` (value: `"instanceName"`)




