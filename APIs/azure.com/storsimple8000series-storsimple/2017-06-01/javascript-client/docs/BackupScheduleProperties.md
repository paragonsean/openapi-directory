# StorSimple8000SeriesManagementClient.BackupScheduleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupType** | **String** | The type of backup which needs to be taken. | 
**lastSuccessfulRun** | **Date** | The last successful backup run which was triggered for the schedule. | [optional] [readonly] 
**retentionCount** | **Number** | The number of backups to be retained. | 
**scheduleRecurrence** | [**ScheduleRecurrence**](ScheduleRecurrence.md) |  | 
**scheduleStatus** | **String** | The schedule status. | 
**startTime** | **Date** | The start time of the schedule. | 



## Enum: BackupTypeEnum


* `LocalSnapshot` (value: `"LocalSnapshot"`)

* `CloudSnapshot` (value: `"CloudSnapshot"`)





## Enum: ScheduleStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




