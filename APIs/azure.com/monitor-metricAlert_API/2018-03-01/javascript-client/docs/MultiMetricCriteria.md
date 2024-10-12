# MonitorManagementClient.MultiMetricCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criterionType** | **String** | Specifies the type of threshold criteria | 
**dimensions** | [**[MetricDimension]**](MetricDimension.md) | List of dimension conditions. | [optional] 
**metricName** | **String** | Name of the metric. | 
**metricNamespace** | **String** | Namespace of the metric. | [optional] 
**name** | **String** | Name of the criteria. | 
**timeAggregation** | **String** | the criteria time aggregation types. | 



## Enum: CriterionTypeEnum


* `StaticThresholdCriterion` (value: `"StaticThresholdCriterion"`)

* `DynamicThresholdCriterion` (value: `"DynamicThresholdCriterion"`)





## Enum: TimeAggregationEnum


* `Average` (value: `"Average"`)

* `Minimum` (value: `"Minimum"`)

* `Maximum` (value: `"Maximum"`)

* `Total` (value: `"Total"`)




