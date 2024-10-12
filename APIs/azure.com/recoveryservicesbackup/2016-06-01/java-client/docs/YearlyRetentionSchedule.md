

# YearlyRetentionSchedule

Yearly retention schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**monthsOfYear** | [**List&lt;MonthsOfYearEnum&gt;**](#List&lt;MonthsOfYearEnum&gt;) | List of the months of year for the yearly retention policy. |  [optional] |
|**retentionDuration** | [**RetentionDuration**](RetentionDuration.md) |  |  [optional] |
|**retentionScheduleDaily** | [**DailyRetentionFormat**](DailyRetentionFormat.md) |  |  [optional] |
|**retentionScheduleFormatType** | [**RetentionScheduleFormatTypeEnum**](#RetentionScheduleFormatTypeEnum) | Retention schedule format for the yearly retention policy. |  [optional] |
|**retentionScheduleWeekly** | [**WeeklyRetentionFormat**](WeeklyRetentionFormat.md) |  |  [optional] |
|**retentionTimes** | **List&lt;OffsetDateTime&gt;** | Retention times for the retention policy. |  [optional] |



## Enum: List&lt;MonthsOfYearEnum&gt;

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| JANUARY | &quot;January&quot; |
| FEBRUARY | &quot;February&quot; |
| MARCH | &quot;March&quot; |
| APRIL | &quot;April&quot; |
| MAY | &quot;May&quot; |
| JUNE | &quot;June&quot; |
| JULY | &quot;July&quot; |
| AUGUST | &quot;August&quot; |
| SEPTEMBER | &quot;September&quot; |
| OCTOBER | &quot;October&quot; |
| NOVEMBER | &quot;November&quot; |
| DECEMBER | &quot;December&quot; |



## Enum: RetentionScheduleFormatTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |



