

# SimpleSchedulePolicy

Simple policy schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scheduleRunDays** | [**List&lt;ScheduleRunDaysEnum&gt;**](#List&lt;ScheduleRunDaysEnum&gt;) | List of days of week this schedule has to be run. |  [optional] |
|**scheduleRunFrequency** | [**ScheduleRunFrequencyEnum**](#ScheduleRunFrequencyEnum) | Frequency of the schedule operation of this policy. |  [optional] |
|**scheduleRunTimes** | **List&lt;OffsetDateTime&gt;** | List of times of day this schedule has to be run. |  [optional] |
|**scheduleWeeklyFrequency** | **Integer** | At every number weeks this schedule has to be run. |  [optional] |



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



