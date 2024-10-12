# BigQueryApi.ArimaSingleModelForecastingMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arimaFittingMetrics** | [**ArimaFittingMetrics**](ArimaFittingMetrics.md) |  | [optional] 
**hasDrift** | **Boolean** | Is arima model fitted with drift or not. It is always false when d is not 1. | [optional] 
**hasHolidayEffect** | **Boolean** | If true, holiday_effect is a part of time series decomposition result. | [optional] 
**hasSpikesAndDips** | **Boolean** | If true, spikes_and_dips is a part of time series decomposition result. | [optional] 
**hasStepChanges** | **Boolean** | If true, step_changes is a part of time series decomposition result. | [optional] 
**nonSeasonalOrder** | [**ArimaOrder**](ArimaOrder.md) |  | [optional] 
**seasonalPeriods** | **[String]** | Seasonal periods. Repeated because multiple periods are supported for one time series. | [optional] 
**timeSeriesId** | **String** | The time_series_id value for this time series. It will be one of the unique values from the time_series_id_column specified during ARIMA model training. Only present when time_series_id_column training option was used. | [optional] 
**timeSeriesIds** | **[String]** | The tuple of time_series_ids identifying this time series. It will be one of the unique tuples of values present in the time_series_id_columns specified during ARIMA model training. Only present when time_series_id_columns training option was used and the order of values here are same as the order of time_series_id_columns. | [optional] 



## Enum: [SeasonalPeriodsEnum]


* `SEASONAL_PERIOD_TYPE_UNSPECIFIED` (value: `"SEASONAL_PERIOD_TYPE_UNSPECIFIED"`)

* `NO_SEASONALITY` (value: `"NO_SEASONALITY"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `YEARLY` (value: `"YEARLY"`)




