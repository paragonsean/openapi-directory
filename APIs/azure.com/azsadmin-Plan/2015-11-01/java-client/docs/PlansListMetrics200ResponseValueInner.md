

# PlansListMetrics200ResponseValueInner

The resource metric set that represents the metrics for a particular resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | End time of the metric. |  [optional] |
|**metricUnit** | [**MetricUnitEnum**](#MetricUnitEnum) | The resource metric unit. |  [optional] |
|**metricValues** | [**List&lt;PlansListMetrics200ResponseValueInnerMetricValuesInner&gt;**](PlansListMetrics200ResponseValueInnerMetricValuesInner.md) | List of metric values. |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of the metric. |  [optional] |
|**timeGrain** | **String** | Timespan of the metric. |  [optional] |



## Enum: MetricUnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



