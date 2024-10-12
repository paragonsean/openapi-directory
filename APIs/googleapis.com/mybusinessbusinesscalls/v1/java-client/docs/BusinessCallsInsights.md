

# BusinessCallsInsights

Insights for calls made to a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregateMetrics** | [**AggregateMetrics**](AggregateMetrics.md) |  |  [optional] |
|**metricType** | [**MetricTypeEnum**](#MetricTypeEnum) | The metric for which the value applies. |  [optional] |
|**name** | **String** | Required. The resource name of the calls insights. Format: locations/{location}/businesscallsinsights |  [optional] |



## Enum: MetricTypeEnum

| Name | Value |
|---- | -----|
| METRIC_TYPE_UNSPECIFIED | &quot;METRIC_TYPE_UNSPECIFIED&quot; |
| AGGREGATE_COUNT | &quot;AGGREGATE_COUNT&quot; |



