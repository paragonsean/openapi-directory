# GoogleMyBusinessApi.DimensionalMetricValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metricOption** | **String** | The option that requested this dimensional value. | [optional] 
**timeDimension** | [**TimeDimension**](TimeDimension.md) |  | [optional] 
**value** | **String** | The value. If no value is set, then the requested data is missing. | [optional] 



## Enum: MetricOptionEnum


* `METRIC_OPTION_UNSPECIFIED` (value: `"METRIC_OPTION_UNSPECIFIED"`)

* `AGGREGATED_TOTAL` (value: `"AGGREGATED_TOTAL"`)

* `AGGREGATED_DAILY` (value: `"AGGREGATED_DAILY"`)

* `BREAKDOWN_DAY_OF_WEEK` (value: `"BREAKDOWN_DAY_OF_WEEK"`)

* `BREAKDOWN_HOUR_OF_DAY` (value: `"BREAKDOWN_HOUR_OF_DAY"`)




