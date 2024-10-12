# BigQueryApi.ArimaForecastingMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arimaFittingMetrics** | [**[ArimaFittingMetrics]**](ArimaFittingMetrics.md) | Arima model fitting metrics. | [optional] 
**arimaSingleModelForecastingMetrics** | [**[ArimaSingleModelForecastingMetrics]**](ArimaSingleModelForecastingMetrics.md) | Repeated as there can be many metric sets (one for each model) in auto-arima and the large-scale case. | [optional] 
**hasDrift** | **[Boolean]** | Whether Arima model fitted with drift or not. It is always false when d is not 1. | [optional] 
**nonSeasonalOrder** | [**[ArimaOrder]**](ArimaOrder.md) | Non-seasonal order. | [optional] 
**seasonalPeriods** | **[String]** | Seasonal periods. Repeated because multiple periods are supported for one time series. | [optional] 
**timeSeriesId** | **[String]** | Id to differentiate different time series for the large-scale case. | [optional] 



## Enum: [SeasonalPeriodsEnum]


* `SEASONAL_PERIOD_TYPE_UNSPECIFIED` (value: `"SEASONAL_PERIOD_TYPE_UNSPECIFIED"`)

* `NO_SEASONALITY` (value: `"NO_SEASONALITY"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `YEARLY` (value: `"YEARLY"`)




