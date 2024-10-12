# CloudMonitoringApi.AggregationFunction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**[Parameter]**](Parameter.md) | Optional. Parameters applied to the aggregation function. Only used for functions that require them. | [optional] 
**type** | **String** | Required. The type of aggregation function, must be one of the following: \&quot;none\&quot; - no function. \&quot;percentile\&quot; - APPROX_QUANTILES() - 1 parameter numeric value \&quot;average\&quot; - AVG() \&quot;count\&quot; - COUNT() \&quot;count-distinct\&quot; - COUNT(DISTINCT) \&quot;count-distinct-approx\&quot; - APPROX_COUNT_DISTINCT() \&quot;max\&quot; - MAX() \&quot;min\&quot; - MIN() \&quot;sum\&quot; - SUM() | [optional] 


