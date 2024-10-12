# AdHybridHealthService.MetricMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The display name for the metric. | [optional] 
**groupings** | [**[MetricGroup]**](MetricGroup.md) | The groupings for the metrics. | [optional] 
**isDefault** | **Boolean** | Indicates if the metric is a default metric or not. | [optional] 
**isDevOps** | **Boolean** | Indicates if the metric is visible to DevOps or not. | [optional] 
**isPerfCounter** | **Boolean** | Indicates if the metric is a performance counter metric or not. | [optional] 
**kind** | **String** | Indicates whether the dashboard to represent the metric is a line, bar,pie, area or donut chart. | [optional] 
**maxValue** | **Number** | The maximum value. | [optional] 
**metricName** | **String** | The metric name | [optional] 
**metricsProcessorClassName** | **String** | The name of the class which retrieve and process the metric. | [optional] 
**minValue** | **Number** | The minimum value. | [optional] 
**valueKind** | **String** | Indicates if the metrics is a rate,value, percent or duration type. | [optional] 


