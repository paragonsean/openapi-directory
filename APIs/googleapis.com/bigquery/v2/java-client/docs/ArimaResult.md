

# ArimaResult

(Auto-)arima fitting result. Wrap everything in ArimaResult for easier refactoring if we want to use model-specific iteration results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arimaModelInfo** | [**List&lt;ArimaModelInfo&gt;**](ArimaModelInfo.md) | This message is repeated because there are multiple arima models fitted in auto-arima. For non-auto-arima model, its size is one. |  [optional] |
|**seasonalPeriods** | [**List&lt;SeasonalPeriodsEnum&gt;**](#List&lt;SeasonalPeriodsEnum&gt;) | Seasonal periods. Repeated because multiple periods are supported for one time series. |  [optional] |



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



