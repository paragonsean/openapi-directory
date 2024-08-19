

# MetricDefinition

Metric definition class specifies the metadata for a metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | the resource identifier of the metric definition. |  [optional] |
|**metricAvailabilities** | [**List&lt;MetricAvailability&gt;**](MetricAvailability.md) | the collection of what aggregation intervals are available to be queried. |  [optional] |
|**name** | [**LocalizableString**](LocalizableString.md) |  |  [optional] |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | the primary aggregation type value defining how to use the values for display. |  [optional] |
|**resourceId** | **String** | the resource identifier of the resource that emitted the metric. |  [optional] |
|**unit** | **Unit** |  |  [optional] |



## Enum: PrimaryAggregationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AVERAGE | &quot;Average&quot; |
| COUNT | &quot;Count&quot; |
| MINIMUM | &quot;Minimum&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| TOTAL | &quot;Total&quot; |



