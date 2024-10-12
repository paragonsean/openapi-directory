

# InvoiceRecurringApiModel

Definition of invoice recurring profile

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfMonth** | **Integer** | Day of month when the recurrance should happen |  [optional] |
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | Day when the recurrance should happen |  [optional] |
|**dueDateInDays** | **Integer** | Total number of days for the client to pay the invoice after issuing it |  [optional] |
|**endOfRecurrance** | **OffsetDateTime** | Indcate the date when the recurrance should stop |  [optional] |
|**month** | **Integer** | Month when the recurrance should happen |  [optional] |
|**recurrancePattern** | [**RecurrancePatternEnum**](#RecurrancePatternEnum) | How often the recurrance occurs |  [optional] |
|**recurranceValue** | **Integer** | Recurring every [value] RecurrancePattern  Ex: Recur every 1 week |  [optional] |
|**startOfRecurrance** | **OffsetDateTime** | Indcate the date when the recurrance has started |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the recurrance |  [optional] |
|**title** | **String** | Title of the recurring profile.   Ex: BRAND PACKAGE - 2017-08-16 - 2018-08-16 |  [optional] |



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



