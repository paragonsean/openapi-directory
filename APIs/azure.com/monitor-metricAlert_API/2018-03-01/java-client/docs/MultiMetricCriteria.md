

# MultiMetricCriteria

The types of conditions for a multi resource alert.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**criterionType** | [**CriterionTypeEnum**](#CriterionTypeEnum) | Specifies the type of threshold criteria |  |
|**dimensions** | [**List&lt;MetricDimension&gt;**](MetricDimension.md) | List of dimension conditions. |  [optional] |
|**metricName** | **String** | Name of the metric. |  |
|**metricNamespace** | **String** | Namespace of the metric. |  [optional] |
|**name** | **String** | Name of the criteria. |  |
|**timeAggregation** | [**TimeAggregationEnum**](#TimeAggregationEnum) | the criteria time aggregation types. |  |



## Enum: CriterionTypeEnum

| Name | Value |
|---- | -----|
| STATIC_THRESHOLD_CRITERION | &quot;StaticThresholdCriterion&quot; |
| DYNAMIC_THRESHOLD_CRITERION | &quot;DynamicThresholdCriterion&quot; |



## Enum: TimeAggregationEnum

| Name | Value |
|---- | -----|
| AVERAGE | &quot;Average&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| TOTAL | &quot;Total&quot; |



