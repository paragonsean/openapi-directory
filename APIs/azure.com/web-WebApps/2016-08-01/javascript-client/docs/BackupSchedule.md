# WebAppsApiClient.BackupSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequencyInterval** | **Number** | How often the backup should be executed (e.g. for weekly backup, this should be set to 7 and FrequencyUnit should be set to Day) | [default to 7]
**frequencyUnit** | **String** | The unit of time for how often the backup should be executed (e.g. for weekly backup, this should be set to Day and FrequencyInterval should be set to 7) | [default to &#39;Day&#39;]
**keepAtLeastOneBackup** | **Boolean** | True if the retention policy should always keep at least one backup in the storage account, regardless how old it is; false otherwise. | [default to true]
**lastExecutionTime** | **Date** | Last time when this schedule was triggered. | [optional] [readonly] 
**retentionPeriodInDays** | **Number** | After how many days backups should be deleted. | [default to 30]
**startTime** | **Date** | When the schedule should start working. | [optional] 



## Enum: FrequencyUnitEnum


* `Day` (value: `"Day"`)

* `Hour` (value: `"Hour"`)




