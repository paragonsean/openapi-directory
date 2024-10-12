

# MetricValue

Represents a single metric value.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolValue** | **Boolean** | A boolean value. |  [optional] |
|**distributionValue** | [**Distribution**](Distribution.md) |  |  [optional] |
|**doubleValue** | **Double** | A double precision floating point value. |  [optional] |
|**endTime** | **String** | The end of the time period over which this metric value&#39;s measurement applies. If not specified, google.api.servicecontrol.v1.Operation.end_time will be used. |  [optional] |
|**int64Value** | **String** | A signed 64-bit integer value. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels describing the metric value. See comments on google.api.servicecontrol.v1.Operation.labels for the overriding relationship. Note that this map must not contain monitored resource labels. |  [optional] |
|**moneyValue** | [**Money**](Money.md) |  |  [optional] |
|**startTime** | **String** | The start of the time period over which this metric value&#39;s measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, google.api.servicecontrol.v1.Operation.start_time will be used. |  [optional] |
|**stringValue** | **String** | A text string value. |  [optional] |



