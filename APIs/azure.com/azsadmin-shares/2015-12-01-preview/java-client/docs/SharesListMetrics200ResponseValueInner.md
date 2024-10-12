

# SharesListMetrics200ResponseValueInner

Metric information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Metric end time. |  [optional] [readonly] |
|**metricUnit** | [**MetricUnitEnum**](#MetricUnitEnum) | Metric unit. |  [optional] |
|**metricValues** | [**List&lt;SharesListMetrics200ResponseValueInnerMetricValuesInner&gt;**](SharesListMetrics200ResponseValueInnerMetricValuesInner.md) | List of metric values. |  [optional] [readonly] |
|**name** | [**SharesListMetricDefinitions200ResponseValueInnerName**](SharesListMetricDefinitions200ResponseValueInnerName.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Metric start time. |  [optional] [readonly] |
|**timeGrain** | **String** | Metric time grain. |  [optional] [readonly] |



## Enum: MetricUnitEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;Count&quot; |
| BYTES | &quot;Bytes&quot; |
| SECONDS | &quot;Seconds&quot; |
| COUNT_PER_SECOND | &quot;CountPerSecond&quot; |
| BYTES_PER_SECOND | &quot;BytesPerSecond&quot; |



