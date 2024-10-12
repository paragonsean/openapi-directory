# Superset.ChartDataProphetOptionsSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceInterval** | **Number** | Width of predicted confidence interval | 
**monthlySeasonality** | **Object** | Should monthly seasonality be applied. An integer value will specify Fourier order of seasonality, &#x60;None&#x60; will automatically detect seasonality. | [optional] 
**periods** | **Number** |  | 
**timeGrain** | **String** | Time grain used to specify time period increments in prediction. Supports [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) durations. | 
**weeklySeasonality** | **Object** | Should weekly seasonality be applied. An integer value will specify Fourier order of seasonality, &#x60;None&#x60; will automatically detect seasonality. | [optional] 
**yearlySeasonality** | **Object** | Should yearly seasonality be applied. An integer value will specify Fourier order of seasonality, &#x60;None&#x60; will automatically detect seasonality. | [optional] 



## Enum: TimeGrainEnum


* `PT1S` (value: `"PT1S"`)

* `PT5S` (value: `"PT5S"`)

* `PT30S` (value: `"PT30S"`)

* `PT1M` (value: `"PT1M"`)

* `PT5M` (value: `"PT5M"`)

* `PT10M` (value: `"PT10M"`)

* `PT15M` (value: `"PT15M"`)

* `PT0.5H` (value: `"PT0.5H"`)

* `PT1H` (value: `"PT1H"`)

* `PT6H` (value: `"PT6H"`)

* `P1D` (value: `"P1D"`)

* `P1W` (value: `"P1W"`)

* `P1M` (value: `"P1M"`)

* `P0.25Y` (value: `"P0.25Y"`)

* `P1Y` (value: `"P1Y"`)

* `1969-12-28T00:00:00Z/P1W` (value: `"1969-12-28T00:00:00Z/P1W"`)

* `1969-12-29T00:00:00Z/P1W` (value: `"1969-12-29T00:00:00Z/P1W"`)

* `P1W/1970-01-03T00:00:00Z` (value: `"P1W/1970-01-03T00:00:00Z"`)

* `P1W/1970-01-04T00:00:00Z` (value: `"P1W/1970-01-04T00:00:00Z"`)




