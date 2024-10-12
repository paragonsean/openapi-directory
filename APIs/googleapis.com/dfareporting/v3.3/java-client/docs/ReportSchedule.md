

# ReportSchedule

The report's schedule. Can only be set if the report's 'dateRange' is a relative date range and the relative date range is not \"TODAY\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Whether the schedule is active or not. Must be set to either true or false. |  [optional] |
|**every** | **Integer** | Defines every how many days, weeks or months the report should be run. Needs to be set when \&quot;repeats\&quot; is either \&quot;DAILY\&quot;, \&quot;WEEKLY\&quot; or \&quot;MONTHLY\&quot;. |  [optional] |
|**expirationDate** | **LocalDate** |  |  [optional] |
|**repeats** | **String** | The interval for which the report is repeated. Note: - \&quot;DAILY\&quot; also requires field \&quot;every\&quot; to be set. - \&quot;WEEKLY\&quot; also requires fields \&quot;every\&quot; and \&quot;repeatsOnWeekDays\&quot; to be set. - \&quot;MONTHLY\&quot; also requires fields \&quot;every\&quot; and \&quot;runsOnDayOfMonth\&quot; to be set.  |  [optional] |
|**repeatsOnWeekDays** | [**List&lt;RepeatsOnWeekDaysEnum&gt;**](#List&lt;RepeatsOnWeekDaysEnum&gt;) | List of week days \&quot;WEEKLY\&quot; on which scheduled reports should run. |  [optional] |
|**runsOnDayOfMonth** | [**RunsOnDayOfMonthEnum**](#RunsOnDayOfMonthEnum) | Enum to define for \&quot;MONTHLY\&quot; scheduled reports whether reports should be repeated on the same day of the month as \&quot;startDate\&quot; or the same day of the week of the month. Example: If &#39;startDate&#39; is Monday, April 2nd 2012 (2012-04-02), \&quot;DAY_OF_MONTH\&quot; would run subsequent reports on the 2nd of every Month, and \&quot;WEEK_OF_MONTH\&quot; would run subsequent reports on the first Monday of the month. |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |



## Enum: List&lt;RepeatsOnWeekDaysEnum&gt;

| Name | Value |
|---- | -----|
| SUNDAY | &quot;SUNDAY&quot; |
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |



## Enum: RunsOnDayOfMonthEnum

| Name | Value |
|---- | -----|
| DAY_OF_MONTH | &quot;DAY_OF_MONTH&quot; |
| WEEK_OF_MONTH | &quot;WEEK_OF_MONTH&quot; |



