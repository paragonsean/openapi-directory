

# MetricRule

Bind API methods to metrics. Binding a method to a metric causes that metric's configured quota behaviors to apply to the method call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricCosts** | **Map&lt;String, String&gt;** | Metrics to update when the selected methods are called, and the associated cost applied to each metric. The key of the map is the metric name, and the values are the amount increased for the metric against which the quota limits are defined. The value must not be negative. |  [optional] |
|**selector** | **String** | Selects the methods to which this rule applies. Refer to selector for syntax details. |  [optional] |



