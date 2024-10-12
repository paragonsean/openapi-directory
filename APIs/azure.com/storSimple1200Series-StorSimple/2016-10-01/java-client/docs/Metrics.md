

# Metrics

Monitoring metric

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List&lt;MetricDimension&gt;**](MetricDimension.md) | The Metric dimension which indicates the source of the metric |  |
|**endTime** | **OffsetDateTime** | The metric end time |  |
|**name** | [**MetricName**](MetricName.md) |  |  |
|**primaryAggregation** | [**PrimaryAggregationEnum**](#PrimaryAggregationEnum) | The metric aggregation type |  |
|**resourceId** | **String** | The id of metric source |  |
|**startTime** | **OffsetDateTime** | The metric start time |  |
|**timeGrain** | **String** | The time grain, time grain indicates frequency of the metric data |  |
|**type** | **String** | The Type of the metric data |  |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of the metric data |  |
|**values** | [**List&lt;MetricData&gt;**](MetricData.md) | The metric data |  |



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



