# RecoveryServicesBackupClient.MonthlyRetentionSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retentionDuration** | [**RetentionDuration**](RetentionDuration.md) |  | [optional] 
**retentionScheduleDaily** | [**DailyRetentionFormat**](DailyRetentionFormat.md) |  | [optional] 
**retentionScheduleFormatType** | **String** | Retention schedule format type for monthly retention policy. | [optional] 
**retentionScheduleWeekly** | [**WeeklyRetentionFormat**](WeeklyRetentionFormat.md) |  | [optional] 
**retentionTimes** | **[Date]** | Retention times of retention policy. | [optional] 



## Enum: RetentionScheduleFormatTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Daily` (value: `"Daily"`)

* `Weekly` (value: `"Weekly"`)




