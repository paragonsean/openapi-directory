

# GoogleCloudApigeeV1MetricAggregation

The optionally aggregated metric to query with its ordering.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregation** | [**AggregationEnum**](#AggregationEnum) | Aggregation function associated with the metric. |  [optional] |
|**name** | **String** | Name of the metric |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | Ordering for this aggregation in the result. For time series this is ignored since the ordering of points depends only on the timestamp, not the values. |  [optional] |



## Enum: AggregationEnum

| Name | Value |
|---- | -----|
| AGGREGATION_FUNCTION_UNSPECIFIED | &quot;AGGREGATION_FUNCTION_UNSPECIFIED&quot; |
| AVG | &quot;AVG&quot; |
| SUM | &quot;SUM&quot; |
| MIN | &quot;MIN&quot; |
| MAX | &quot;MAX&quot; |
| COUNT_DISTINCT | &quot;COUNT_DISTINCT&quot; |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| ORDER_UNSPECIFIED | &quot;ORDER_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |



