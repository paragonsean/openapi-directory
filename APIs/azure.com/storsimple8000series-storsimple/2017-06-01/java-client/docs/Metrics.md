

# Metrics

The monitoring metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List&lt;MetricDimension&gt;**](MetricDimension.md) | The metric dimensions. |  [optional] |
|**endTime** | **OffsetDateTime** | The end time of the metric data. |  [optional] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**primaryAggregation** | [**PrimaryAggregationEnum**](#PrimaryAggregationEnum) | The metric aggregation type. |  [optional] |
|**resourceId** | **String** | The ID of metric source. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the metric data. |  [optional] |
|**timeGrain** | **String** | The time granularity of the metric data. |  [optional] |
|**type** | **String** | The type of the metric data. |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of the metric data. |  [optional] |
|**values** | [**List&lt;MetricData&gt;**](MetricData.md) | The list of the metric data. |  [optional] |



## Enum: PrimaryAggregationEnum

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



