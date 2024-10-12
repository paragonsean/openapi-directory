# WebSiteManagementClient.BackupSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequencyInterval** | **Number** | How often should be the backup executed (e.g. for weekly backup, this should be set to 7 and FrequencyUnit should be set to Day) | [optional] 
**frequencyUnit** | **String** | How often should be the backup executed (e.g. for weekly backup, this should be set to Day and FrequencyInterval should be set to 7) | 
**keepAtLeastOneBackup** | **Boolean** | True if the retention policy should always keep at least one backup in the storage account, regardless how old it is; false otherwise. | [optional] 
**lastExecutionTime** | **Date** | The last time when this schedule was triggered | [optional] 
**retentionPeriodInDays** | **Number** | After how many days backups should be deleted | [optional] 
**startTime** | **Date** | When the schedule should start working | [optional] 



## Enum: FrequencyUnitEnum


* `Day` (value: `"Day"`)

* `Hour` (value: `"Hour"`)




