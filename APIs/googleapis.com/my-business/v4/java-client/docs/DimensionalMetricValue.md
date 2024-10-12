

# DimensionalMetricValue

A value for a single metric with a given time dimension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metricOption** | [**MetricOptionEnum**](#MetricOptionEnum) | The option that requested this dimensional value. |  [optional] |
|**timeDimension** | [**TimeDimension**](TimeDimension.md) |  |  [optional] |
|**value** | **String** | The value. If no value is set, then the requested data is missing. |  [optional] |



## Enum: MetricOptionEnum

| Name | Value |
|---- | -----|
| METRIC_OPTION_UNSPECIFIED | &quot;METRIC_OPTION_UNSPECIFIED&quot; |
| AGGREGATED_TOTAL | &quot;AGGREGATED_TOTAL&quot; |
| AGGREGATED_DAILY | &quot;AGGREGATED_DAILY&quot; |
| BREAKDOWN_DAY_OF_WEEK | &quot;BREAKDOWN_DAY_OF_WEEK&quot; |
| BREAKDOWN_HOUR_OF_DAY | &quot;BREAKDOWN_HOUR_OF_DAY&quot; |



