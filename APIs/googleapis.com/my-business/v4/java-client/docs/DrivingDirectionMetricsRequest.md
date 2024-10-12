

# DrivingDirectionMetricsRequest

A request for driving direction insights.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | The BCP 47 code for the language. If a language code is not provided, it defaults to English. |  [optional] |
|**numDays** | [**NumDaysEnum**](#NumDaysEnum) | The number of days to aggregate data for. Results returned will be available data over the last number of requested days. Valid values are 7, 30, and 90. |  [optional] |



## Enum: NumDaysEnum

| Name | Value |
|---- | -----|
| SEVEN | &quot;SEVEN&quot; |
| THIRTY | &quot;THIRTY&quot; |
| NINETY | &quot;NINETY&quot; |



