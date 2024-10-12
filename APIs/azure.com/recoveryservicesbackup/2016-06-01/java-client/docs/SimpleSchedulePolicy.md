

# SimpleSchedulePolicy

Simple policy schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scheduleRunDays** | [**List&lt;ScheduleRunDaysEnum&gt;**](#List&lt;ScheduleRunDaysEnum&gt;) | This list is the days of the week when the schedule runs. |  [optional] |
|**scheduleRunFrequency** | [**ScheduleRunFrequencyEnum**](#ScheduleRunFrequencyEnum) | Defines the frequency interval (daily or weekly) for the schedule policy. |  [optional] |
|**scheduleRunTimes** | **List&lt;OffsetDateTime&gt;** | List of times, during a day, when the schedule runs. |  [optional] |
|**scheduleWeeklyFrequency** | **Integer** | The number of times per week the schedule runs. |  [optional] |



## Enum: List&lt;ScheduleRunDaysEnum&gt;

| Name | Value |
|---- | -----|
| SUNDAY | &quot;Sunday&quot; |
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |



## Enum: ScheduleRunFrequencyEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |



