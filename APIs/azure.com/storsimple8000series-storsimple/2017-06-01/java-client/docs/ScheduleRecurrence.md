

# ScheduleRecurrence

The schedule recurrence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recurrenceType** | [**RecurrenceTypeEnum**](#RecurrenceTypeEnum) | The recurrence type. |  |
|**recurrenceValue** | **Integer** | The recurrence value. |  |
|**weeklyDaysList** | [**List&lt;WeeklyDaysListEnum&gt;**](#List&lt;WeeklyDaysListEnum&gt;) | The week days list. Applicable only for schedules of recurrence type &#39;weekly&#39;. |  [optional] |



## Enum: RecurrenceTypeEnum

| Name | Value |
|---- | -----|
| MINUTES | &quot;Minutes&quot; |
| HOURLY | &quot;Hourly&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |



## Enum: List&lt;WeeklyDaysListEnum&gt;

| Name | Value |
|---- | -----|
| SUNDAY | &quot;Sunday&quot; |
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |



