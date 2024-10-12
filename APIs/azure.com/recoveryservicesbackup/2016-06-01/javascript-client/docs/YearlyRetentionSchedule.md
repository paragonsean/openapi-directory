# RecoveryServicesBackupClient.YearlyRetentionSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthsOfYear** | **[String]** | List of the months of year for the yearly retention policy. | [optional] 
**retentionDuration** | [**RetentionDuration**](RetentionDuration.md) |  | [optional] 
**retentionScheduleDaily** | [**DailyRetentionFormat**](DailyRetentionFormat.md) |  | [optional] 
**retentionScheduleFormatType** | **String** | Retention schedule format for the yearly retention policy. | [optional] 
**retentionScheduleWeekly** | [**WeeklyRetentionFormat**](WeeklyRetentionFormat.md) |  | [optional] 
**retentionTimes** | **[Date]** | Retention times for the retention policy. | [optional] 



## Enum: [MonthsOfYearEnum]


* `Invalid` (value: `"Invalid"`)

* `January` (value: `"January"`)

* `February` (value: `"February"`)

* `March` (value: `"March"`)

* `April` (value: `"April"`)

* `May` (value: `"May"`)

* `June` (value: `"June"`)

* `July` (value: `"July"`)

* `August` (value: `"August"`)

* `September` (value: `"September"`)

* `October` (value: `"October"`)

* `November` (value: `"November"`)

* `December` (value: `"December"`)





## Enum: RetentionScheduleFormatTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Daily` (value: `"Daily"`)

* `Weekly` (value: `"Weekly"`)




