

# Schedule

Defines scheduling parameters for automatically creating Backups via this BackupPlan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cronSchedule** | **String** | Optional. A standard [cron](https://wikipedia.com/wiki/cron) string that defines a repeating schedule for creating Backups via this BackupPlan. This is mutually exclusive with the rpo_config field since at most one schedule can be defined for a BackupPlan. If this is defined, then backup_retain_days must also be defined. Default (empty): no automatic backup creation will occur. |  [optional] |
|**paused** | **Boolean** | Optional. This flag denotes whether automatic Backup creation is paused for this BackupPlan. Default: False |  [optional] |



