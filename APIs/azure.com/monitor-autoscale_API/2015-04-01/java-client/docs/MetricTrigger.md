

# MetricTrigger

The trigger that results in a scaling action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricName** | **String** | the name of the metric that defines what the rule monitors. |  |
|**metricResourceUri** | **String** | the resource identifier of the resource the rule monitors. |  |
|**operator** | [**OperatorEnum**](#OperatorEnum) | the operator that is used to compare the metric data and the threshold. |  |
|**statistic** | [**StatisticEnum**](#StatisticEnum) | the metric statistic type. How the metrics from multiple instances are combined. |  |
|**threshold** | **Double** | the threshold of the metric that triggers the scale action. |  |
|**timeAggregation** | [**TimeAggregationEnum**](#TimeAggregationEnum) | time aggregation type. How the data that is collected should be combined over time. The default value is Average. |  |
|**timeGrain** | **String** | the granularity of metrics the rule monitors. Must be one of the predefined values returned from metric definitions for the metric. Must be between 12 hours and 1 minute. |  |
|**timeWindow** | **String** | the range of time in which instance data is collected. This value must be greater than the delay in metric collection, which can vary from resource-to-resource. Must be between 12 hours and 5 minutes. |  |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| EQUALS | &quot;Equals&quot; |
| NOT_EQUALS | &quot;NotEquals&quot; |
| GREATER_THAN | &quot;GreaterThan&quot; |
| GREATER_THAN_OR_EQUAL | &quot;GreaterThanOrEqual&quot; |
| LESS_THAN | &quot;LessThan&quot; |
| LESS_THAN_OR_EQUAL | &quot;LessThanOrEqual&quot; |



## Enum: StatisticEnum

| Name | Value |
|---- | -----|
| AVERAGE | &quot;Average&quot; |
| MIN | &quot;Min&quot; |
| MAX | &quot;Max&quot; |
| SUM | &quot;Sum&quot; |



## Enum: TimeAggregationEnum

| Name | Value |
|---- | -----|
| AVERAGE | &quot;Average&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| TOTAL | &quot;Total&quot; |
| COUNT | &quot;Count&quot; |
| LAST | &quot;Last&quot; |



