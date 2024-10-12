

# Event


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | The amount of the event. |  [optional] |
|**amountInBaseCurrency** | **BigDecimal** | The amount of the event in the user&#39;s base currency. |  [optional] |
|**category** | [**Category**](Category.md) |  |  [optional] |
|**colour** | **String** | The CSS hex-style colour of the event. |  [optional] |
|**currencyCode** | **String** | The currency code of the event. |  [optional] |
|**date** | **String** | The date of the event. |  [optional] |
|**id** | **String** | The unique identifier of the event. |  [optional] |
|**infiniteSeries** | **Boolean** | Whether the event repeats and does not have an end date. |  [optional] |
|**note** | **String** | The note of the event. |  [optional] |
|**repeatInterval** | **Integer** | The repeat interval of how often the event takes place. |  [optional] |
|**repeatType** | [**RepeatTypeEnum**](#RepeatTypeEnum) | The repeat type of the event. |  [optional] |
|**scenario** | [**Scenario**](Scenario.md) |  |  [optional] |
|**seriesId** | **Integer** | The unique identifier of the series that the event belongs to. |  [optional] |
|**seriesStartId** | **String** | The unique identifier of the series followed by the series&#39;s start date. |  [optional] |



## Enum: RepeatTypeEnum

| Name | Value |
|---- | -----|
| ONCE | &quot;once&quot; |
| DAILY | &quot;daily&quot; |
| WEEKLY | &quot;weekly&quot; |
| FORTNIGHTLY | &quot;fortnightly&quot; |
| MONTHLY | &quot;monthly&quot; |
| YEARLY | &quot;yearly&quot; |
| EACH_WEEKDAY | &quot;each weekday&quot; |



