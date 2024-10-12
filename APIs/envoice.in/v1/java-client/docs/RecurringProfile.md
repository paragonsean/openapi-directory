

# RecurringProfile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfMonth** | **Integer** |  |  [optional] |
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) |  |  [optional] |
|**dueDateInDays** | **Integer** |  |  [optional] |
|**endOfRecurrance** | **OffsetDateTime** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**invoiceId** | **Integer** |  |  [optional] |
|**month** | **Integer** |  |  [optional] |
|**recurrancePattern** | [**RecurrancePatternEnum**](#RecurrancePatternEnum) |  |  [optional] |
|**recurranceValue** | **Integer** |  |  [optional] |
|**startOfRecurrance** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| SUNDAY | &quot;Sunday&quot; |
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |



## Enum: RecurrancePatternEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| YEARLY | &quot;Yearly&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;Pending&quot; |
| ACTIVE | &quot;Active&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FINISHED | &quot;Finished&quot; |



