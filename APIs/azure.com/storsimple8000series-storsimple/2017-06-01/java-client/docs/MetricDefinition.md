

# MetricDefinition

The monitoring metric definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The category of the metric. |  [optional] |
|**dimensions** | [**List&lt;MetricDimension&gt;**](MetricDimension.md) | The available metric dimensions. |  [optional] |
|**metricAvailabilities** | [**List&lt;MetricAvailablity&gt;**](MetricAvailablity.md) | The available metric granularities. |  [optional] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | The metric aggregation type. |  [optional] |
|**resourceId** | **String** | The metric source ID. |  [optional] |
|**type** | **String** | The metric definition type. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The metric unit. |  [optional] |



## Enum: PrimaryAggregationTypeEnum

| Name | Value |
|---- | -----|
| AVERAGE | &quot;Average&quot; |
| LAST | &quot;Last&quot; |
| MAXIMUM | &quot;Maximum&quot; |
| MINIMUM | &quot;Minimum&quot; |
| NONE | &quot;None&quot; |
| TOTAL | &quot;Total&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| BYTES | &quot;Bytes&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |
| COUNT | &quot;Count&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| PERCENT | &quot;Percent&quot; |
| SECONDS | &quot;Seconds&quot; |



