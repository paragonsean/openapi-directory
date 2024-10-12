# AnomalyFinderClient.Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customInterval** | **Number** | Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes, request can be set as {\&quot;granularity\&quot;:\&quot;minutely\&quot;, \&quot;customInterval\&quot;:5}. | [optional] 
**granularity** | **String** | Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid. | 
**maxAnomalyRatio** | **Number** | Optional argument, advanced model parameter, max anomaly ratio in a time series. | [optional] 
**period** | **Number** | Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically. | [optional] 
**sensitivity** | **Number** | Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted. | [optional] 
**series** | [**[Point]**](Point.md) | Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned. | 



## Enum: GranularityEnum


* `yearly` (value: `"yearly"`)

* `monthly` (value: `"monthly"`)

* `weekly` (value: `"weekly"`)

* `daily` (value: `"daily"`)

* `hourly` (value: `"hourly"`)

* `minutely` (value: `"minutely"`)




