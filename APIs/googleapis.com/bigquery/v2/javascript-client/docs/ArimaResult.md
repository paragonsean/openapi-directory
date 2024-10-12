# BigQueryApi.ArimaResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arimaModelInfo** | [**[ArimaModelInfo]**](ArimaModelInfo.md) | This message is repeated because there are multiple arima models fitted in auto-arima. For non-auto-arima model, its size is one. | [optional] 
**seasonalPeriods** | **[String]** | Seasonal periods. Repeated because multiple periods are supported for one time series. | [optional] 



## Enum: [SeasonalPeriodsEnum]


* `SEASONAL_PERIOD_TYPE_UNSPECIFIED` (value: `"SEASONAL_PERIOD_TYPE_UNSPECIFIED"`)

* `NO_SEASONALITY` (value: `"NO_SEASONALITY"`)

* `DAILY` (value: `"DAILY"`)

* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)

* `QUARTERLY` (value: `"QUARTERLY"`)

* `YEARLY` (value: `"YEARLY"`)




