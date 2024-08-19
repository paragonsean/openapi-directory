

# WeeklySchedule

A weekly schedule starts a backup at prescribed start times within a day, for the specified days of the week. The weekly schedule message is flexible and can be used to create many types of schedules. For example, to have a daily backup that starts at 22:00, configure the `start_times` field to have one element \"22:00\" and the `days_of_week` field to have all seven days of the week.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**daysOfWeek** | [**List&lt;DaysOfWeekEnum&gt;**](#List&lt;DaysOfWeekEnum&gt;) | The days of the week to perform a backup. If this field is left empty, the default of every day of the week is used. |  [optional] |
|**startTimes** | [**List&lt;GoogleTypeTimeOfDay&gt;**](GoogleTypeTimeOfDay.md) | The times during the day to start a backup. The start times are assumed to be in UTC and to be an exact hour (e.g., 04:00:00). If no start times are provided, a single fixed start time is chosen arbitrarily. |  [optional] |



## Enum: List&lt;DaysOfWeekEnum&gt;

| Name | Value |
|---- | -----|
| DAY_OF_WEEK_UNSPECIFIED | &quot;DAY_OF_WEEK_UNSPECIFIED&quot; |
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



