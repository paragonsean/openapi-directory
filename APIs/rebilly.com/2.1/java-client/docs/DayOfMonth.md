

# DayOfMonth


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**day** | **Integer** | The day of the month when event will be scheduled. Be aware if the month has less days, the last day of the month will be selected.  |  |
|**time** | **String** | Extended ISO-8601 format of time. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| INTELLIGENT | &quot;intelligent&quot; |
| IMMEDIATELY | &quot;immediately&quot; |
| DATE_INTERVAL | &quot;date-interval&quot; |
| DAY_OF_MONTH | &quot;day-of-month&quot; |
| DAY_OF_WEEK | &quot;day-of-week&quot; |



