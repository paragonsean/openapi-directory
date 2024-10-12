

# Metric

Database metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The end time for the metric (ISO-8601 format). |  [optional] [readonly] |
|**metricValues** | [**List&lt;MetricValue&gt;**](MetricValue.md) | The metric values for the specified time window and timestep. |  [optional] [readonly] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The start time for the metric (ISO-8601 format). |  [optional] [readonly] |
|**timeGrain** | **String** | The time step to be used to summarize the metric values. |  [optional] [readonly] |
|**unit** | [**UnitEnum**](#UnitEnum) | The unit of the metric. |  [optional] [readonly] |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;count&quot; |
| BYTES | &quot;bytes&quot; |
| SECONDS | &quot;seconds&quot; |
| PERCENT | &quot;percent&quot; |
| COUNT_PER_SECOND | &quot;countPerSecond&quot; |
| BYTES_PER_SECOND | &quot;bytesPerSecond&quot; |



