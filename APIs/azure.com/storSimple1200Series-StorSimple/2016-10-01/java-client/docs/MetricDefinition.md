

# MetricDefinition

Monitoring metric definition represents the metadata of the metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List&lt;MetricDimension&gt;**](MetricDimension.md) | The supported dimensions |  |
|**metricAvailabilities** | [**List&lt;MetricAvailablity&gt;**](MetricAvailablity.md) | The available metric granularities |  |
|**name** | [**MetricName**](MetricName.md) |  |  |
|**primaryAggregationType** | [**PrimaryAggregationTypeEnum**](#PrimaryAggregationTypeEnum) | The metric aggregation type |  |
|**resourceId** | **String** | The metric source id |  |
|**type** | **String** | The metric definition type |  |
|**unit** | [**UnitEnum**](#UnitEnum) | The metric unit |  |



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



