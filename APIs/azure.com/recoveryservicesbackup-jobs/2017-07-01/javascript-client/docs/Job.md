# RecoveryServicesBackupClient.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityId** | **String** | ActivityId of job. | [optional] 
**backupManagementType** | **String** | Backup management type to execute the current job. | [optional] 
**endTime** | **Date** | The end time. | [optional] 
**entityFriendlyName** | **String** | Friendly name of the entity on which the current job is executing. | [optional] 
**jobType** | **String** | This property will be used as the discriminator for deciding the specific types in the polymorhpic chain of types. | 
**operation** | **String** | The operation name. | [optional] 
**startTime** | **Date** | The start time. | [optional] 
**status** | **String** | Job status. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)




