# MonitorManagementClient.MetricTrigger

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricName** | **String** | the name of the metric that defines what the rule monitors. | 
**metricResourceUri** | **String** | the resource identifier of the resource the rule monitors. | 
**operator** | **String** | the operator that is used to compare the metric data and the threshold. | 
**statistic** | **String** | the metric statistic type. How the metrics from multiple instances are combined. | 
**threshold** | **Number** | the threshold of the metric that triggers the scale action. | 
**timeAggregation** | **String** | time aggregation type. How the data that is collected should be combined over time. The default value is Average. | 
**timeGrain** | **String** | the granularity of metrics the rule monitors. Must be one of the predefined values returned from metric definitions for the metric. Must be between 12 hours and 1 minute. | 
**timeWindow** | **String** | the range of time in which instance data is collected. This value must be greater than the delay in metric collection, which can vary from resource-to-resource. Must be between 12 hours and 5 minutes. | 



## Enum: OperatorEnum


* `Equals` (value: `"Equals"`)

* `NotEquals` (value: `"NotEquals"`)

* `GreaterThan` (value: `"GreaterThan"`)

* `GreaterThanOrEqual` (value: `"GreaterThanOrEqual"`)

* `LessThan` (value: `"LessThan"`)

* `LessThanOrEqual` (value: `"LessThanOrEqual"`)





## Enum: StatisticEnum


* `Average` (value: `"Average"`)

* `Min` (value: `"Min"`)

* `Max` (value: `"Max"`)

* `Sum` (value: `"Sum"`)





## Enum: TimeAggregationEnum


* `Average` (value: `"Average"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Total` (value: `"Total"`)

* `Count` (value: `"Count"`)

* `Last` (value: `"Last"`)




