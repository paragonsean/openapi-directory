# CloudMonitoringApi.PickTimeSeriesFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **String** | How to use the ranking to select time series that pass through the filter. | [optional] 
**interval** | [**Interval**](Interval.md) |  | [optional] 
**numTimeSeries** | **Number** | How many time series to allow to pass through the filter. | [optional] 
**rankingMethod** | **String** | ranking_method is applied to each time series independently to produce the value which will be used to compare the time series to other time series. | [optional] 



## Enum: DirectionEnum


* `DIRECTION_UNSPECIFIED` (value: `"DIRECTION_UNSPECIFIED"`)

* `TOP` (value: `"TOP"`)

* `BOTTOM` (value: `"BOTTOM"`)





## Enum: RankingMethodEnum


* `UNSPECIFIED` (value: `"METHOD_UNSPECIFIED"`)

* `MEAN` (value: `"METHOD_MEAN"`)

* `MAX` (value: `"METHOD_MAX"`)

* `MIN` (value: `"METHOD_MIN"`)

* `SUM` (value: `"METHOD_SUM"`)

* `LATEST` (value: `"METHOD_LATEST"`)




