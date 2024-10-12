

# BackupScheduleProperties

The properties of the backup schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupType** | [**BackupTypeEnum**](#BackupTypeEnum) | The type of backup which needs to be taken. |  |
|**lastSuccessfulRun** | **OffsetDateTime** | The last successful backup run which was triggered for the schedule. |  [optional] [readonly] |
|**retentionCount** | **Long** | The number of backups to be retained. |  |
|**scheduleRecurrence** | [**ScheduleRecurrence**](ScheduleRecurrence.md) |  |  |
|**scheduleStatus** | [**ScheduleStatusEnum**](#ScheduleStatusEnum) | The schedule status. |  |
|**startTime** | **OffsetDateTime** | The start time of the schedule. |  |



## Enum: BackupTypeEnum

| Name | Value |
|---- | -----|
| LOCAL_SNAPSHOT | &quot;LocalSnapshot&quot; |
| CLOUD_SNAPSHOT | &quot;CloudSnapshot&quot; |



## Enum: ScheduleStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



