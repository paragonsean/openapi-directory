

# EventsIdPutRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | The amount of the event. A positive amount is a credit, and a negative amount is a debit. |  [optional] |
|**behaviour** | [**BehaviourEnum**](#BehaviourEnum) | Whether the update applies only to this event, to all events within the series from this event or to all events within the series. |  |
|**note** | **String** | A note for the event. |  [optional] |
|**repeatInterval** | **Integer** | The repeat interval of the event. |  [optional] |
|**repeatType** | [**RepeatTypeEnum**](#RepeatTypeEnum) | The repeat type of the event. |  [optional] |



## Enum: BehaviourEnum

| Name | Value |
|---- | -----|
| ONE | &quot;one&quot; |
| FORWARD | &quot;forward&quot; |
| ALL | &quot;all&quot; |



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



