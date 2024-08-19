

# PercentileMetric

Percentile Metric data

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The end time for the metric (ISO-8601 format). |  [optional] [readonly] |
|**metricValues** | [**List&lt;PercentileMetricValue&gt;**](PercentileMetricValue.md) | The percentile metric values for the specified time window and timestep. |  [optional] [readonly] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The start time for the metric (ISO-8601 format). |  [optional] [readonly] |
|**timeGrain** | **String** | The time grain to be used to summarize the metric values. |  [optional] [readonly] |
|**unit** | **UnitType** |  |  [optional] |



