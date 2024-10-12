

# AggregationFunction

Preview: An identifier for an aggregation function. Aggregation functions are SQL functions that group or transform data from multiple points to a single point. This is a preview feature and may be subject to change before final release.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameters** | [**List&lt;Parameter&gt;**](Parameter.md) | Optional. Parameters applied to the aggregation function. Only used for functions that require them. |  [optional] |
|**type** | **String** | Required. The type of aggregation function, must be one of the following: \&quot;none\&quot; - no function. \&quot;percentile\&quot; - APPROX_QUANTILES() - 1 parameter numeric value \&quot;average\&quot; - AVG() \&quot;count\&quot; - COUNT() \&quot;count-distinct\&quot; - COUNT(DISTINCT) \&quot;count-distinct-approx\&quot; - APPROX_COUNT_DISTINCT() \&quot;max\&quot; - MAX() \&quot;min\&quot; - MIN() \&quot;sum\&quot; - SUM() |  [optional] |



