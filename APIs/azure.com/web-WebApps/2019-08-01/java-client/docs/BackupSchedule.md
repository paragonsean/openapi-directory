

# BackupSchedule

Description of a backup schedule. Describes how often should be the backup performed and what should be the retention policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequencyInterval** | **Integer** | How often the backup should be executed (e.g. for weekly backup, this should be set to 7 and FrequencyUnit should be set to Day) |  |
|**frequencyUnit** | [**FrequencyUnitEnum**](#FrequencyUnitEnum) | The unit of time for how often the backup should be executed (e.g. for weekly backup, this should be set to Day and FrequencyInterval should be set to 7) |  |
|**keepAtLeastOneBackup** | **Boolean** | True if the retention policy should always keep at least one backup in the storage account, regardless how old it is; false otherwise. |  |
|**lastExecutionTime** | **OffsetDateTime** | Last time when this schedule was triggered. |  [optional] [readonly] |
|**retentionPeriodInDays** | **Integer** | After how many days backups should be deleted. |  |
|**startTime** | **OffsetDateTime** | When the schedule should start working. |  [optional] |



## Enum: FrequencyUnitEnum

| Name | Value |
|---- | -----|
| DAY | &quot;Day&quot; |
| HOUR | &quot;Hour&quot; |



