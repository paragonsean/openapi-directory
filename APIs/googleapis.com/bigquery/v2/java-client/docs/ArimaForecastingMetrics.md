

# ArimaForecastingMetrics

Model evaluation metrics for ARIMA forecasting models.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arimaFittingMetrics** | [**List&lt;ArimaFittingMetrics&gt;**](ArimaFittingMetrics.md) | Arima model fitting metrics. |  [optional] |
|**arimaSingleModelForecastingMetrics** | [**List&lt;ArimaSingleModelForecastingMetrics&gt;**](ArimaSingleModelForecastingMetrics.md) | Repeated as there can be many metric sets (one for each model) in auto-arima and the large-scale case. |  [optional] |
|**hasDrift** | **List&lt;Boolean&gt;** | Whether Arima model fitted with drift or not. It is always false when d is not 1. |  [optional] |
|**nonSeasonalOrder** | [**List&lt;ArimaOrder&gt;**](ArimaOrder.md) | Non-seasonal order. |  [optional] |
|**seasonalPeriods** | [**List&lt;SeasonalPeriodsEnum&gt;**](#List&lt;SeasonalPeriodsEnum&gt;) | Seasonal periods. Repeated because multiple periods are supported for one time series. |  [optional] |
|**timeSeriesId** | **List&lt;String&gt;** | Id to differentiate different time series for the large-scale case. |  [optional] |



## Enum: List&lt;SeasonalPeriodsEnum&gt;

| Name | Value |
|---- | -----|
| SEASONAL_PERIOD_TYPE_UNSPECIFIED | &quot;SEASONAL_PERIOD_TYPE_UNSPECIFIED&quot; |
| NO_SEASONALITY | &quot;NO_SEASONALITY&quot; |
| DAILY | &quot;DAILY&quot; |
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |
| QUARTERLY | &quot;QUARTERLY&quot; |
| YEARLY | &quot;YEARLY&quot; |



