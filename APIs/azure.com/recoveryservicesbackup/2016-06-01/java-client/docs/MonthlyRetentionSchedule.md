

# MonthlyRetentionSchedule

The monthly retention schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**retentionDuration** | [**RetentionDuration**](RetentionDuration.md) |  |  [optional] |
|**retentionScheduleDaily** | [**DailyRetentionFormat**](DailyRetentionFormat.md) |  |  [optional] |
|**retentionScheduleFormatType** | [**RetentionScheduleFormatTypeEnum**](#RetentionScheduleFormatTypeEnum) | Retention schedule format type for monthly retention policy. |  [optional] |
|**retentionScheduleWeekly** | [**WeeklyRetentionFormat**](WeeklyRetentionFormat.md) |  |  [optional] |
|**retentionTimes** | **List&lt;OffsetDateTime&gt;** | Retention times of the retention policy. |  [optional] |



## Enum: RetentionScheduleFormatTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |



