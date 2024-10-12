

# JobRecurrenceSchedule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hours** | **List&lt;Integer&gt;** | Gets or sets the hours of the day that the job should execute at. |  [optional] |
|**minutes** | **List&lt;Integer&gt;** | Gets or sets the minutes of the hour that the job should execute at. |  [optional] |
|**monthDays** | **List&lt;Integer&gt;** | Gets or sets the days of the month that the job should execute on. Must be between 1 and 31. |  [optional] |
|**monthlyOccurrences** | [**List&lt;JobRecurrenceScheduleMonthlyOccurrence&gt;**](JobRecurrenceScheduleMonthlyOccurrence.md) | Gets or sets the occurrences of days within a month. |  [optional] |
|**weekDays** | [**List&lt;WeekDaysEnum&gt;**](#List&lt;WeekDaysEnum&gt;) | Gets or sets the days of the week that the job should execute on. |  [optional] |



## Enum: List&lt;WeekDaysEnum&gt;

| Name | Value |
|---- | -----|
| SUNDAY | &quot;Sunday&quot; |
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |



