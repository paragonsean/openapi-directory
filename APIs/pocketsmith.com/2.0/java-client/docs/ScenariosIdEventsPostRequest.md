

# ScenariosIdEventsPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | The amount of the event. A positive amount is a credit, and a negative amount is a debit. |  |
|**categoryId** | **Integer** | The unique identifier of the category for the event. |  |
|**date** | **String** | The starting date of the event. |  |
|**note** | **String** | A note for the event. |  [optional] |
|**repeatInterval** | **Integer** | The repeat interval of the event. |  [optional] |
|**repeatType** | [**RepeatTypeEnum**](#RepeatTypeEnum) | The repeat type of the event. |  |



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



