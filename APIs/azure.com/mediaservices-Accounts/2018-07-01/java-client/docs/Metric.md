

# Metric

A metric emitted by service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationType** | [**AggregationTypeEnum**](#AggregationTypeEnum) | The metric aggregation type |  [optional] [readonly] |
|**dimensions** | [**List&lt;MetricDimension&gt;**](MetricDimension.md) | The metric dimensions. |  [optional] [readonly] |
|**displayDescription** | **String** | The metric display description. |  [optional] [readonly] |
|**displayName** | **String** | The metric display name. |  [optional] [readonly] |
|**name** | **String** | The metric name. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | The metric unit |  [optional] [readonly] |



## Enum: AggregationTypeEnum

| Name | Value |
|---- | -----|
| AVERAGE | &quot;Average&quot; |
| COUNT | &quot;Count&quot; |
| TOTAL | &quot;Total&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| BYTES | &quot;Bytes&quot; |
| COUNT | &quot;Count&quot; |
| MILLISECONDS | &quot;Milliseconds&quot; |



