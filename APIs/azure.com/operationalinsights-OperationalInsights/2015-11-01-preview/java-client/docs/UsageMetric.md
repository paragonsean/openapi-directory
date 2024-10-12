

# UsageMetric

A metric describing the usage of a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentValue** | **Double** | The current value of the metric. |  [optional] |
|**limit** | **Double** | The quota limit for the metric. |  [optional] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**nextResetTime** | **OffsetDateTime** | The time that the metric&#39;s value will reset. |  [optional] |
|**quotaPeriod** | **String** | The quota period that determines the length of time between value resets. |  [optional] |
|**unit** | **String** | The units used for the metric. |  [optional] |



