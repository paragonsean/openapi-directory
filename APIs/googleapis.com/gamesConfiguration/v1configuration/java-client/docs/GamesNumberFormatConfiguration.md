

# GamesNumberFormatConfiguration

A number format resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | The curreny code string. Only used for CURRENCY format type. |  [optional] |
|**numDecimalPlaces** | **Integer** | The number of decimal places for number. Only used for NUMERIC format type. |  [optional] |
|**numberFormatType** | [**NumberFormatTypeEnum**](#NumberFormatTypeEnum) | The formatting for the number. |  [optional] |
|**suffix** | [**GamesNumberAffixConfiguration**](GamesNumberAffixConfiguration.md) |  |  [optional] |



## Enum: NumberFormatTypeEnum

| Name | Value |
|---- | -----|
| NUMBER_FORMAT_TYPE_UNSPECIFIED | &quot;NUMBER_FORMAT_TYPE_UNSPECIFIED&quot; |
| NUMERIC | &quot;NUMERIC&quot; |
| TIME_DURATION | &quot;TIME_DURATION&quot; |
| CURRENCY | &quot;CURRENCY&quot; |



