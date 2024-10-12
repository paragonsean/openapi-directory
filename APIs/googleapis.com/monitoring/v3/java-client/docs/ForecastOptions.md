

# ForecastOptions

Options used when forecasting the time series and testing the predicted value against the threshold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forecastHorizon** | **String** | Required. The length of time into the future to forecast whether a time series will violate the threshold. If the predicted value is found to violate the threshold, and the violation is observed in all forecasts made for the configured duration, then the time series is considered to be failing. The forecast horizon can range from 1 hour to 60 hours. |  [optional] |



