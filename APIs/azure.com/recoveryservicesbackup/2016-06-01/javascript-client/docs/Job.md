# RecoveryServicesBackupClient.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityId** | **String** | ActivityId of job. | [optional] 
**backupManagementType** | **String** | The backup management type for the current job. | [optional] 
**endTime** | **Date** | The end time. | [optional] 
**entityFriendlyName** | **String** | The friendly name of the entity on which the current job is executing. | [optional] 
**jobType** | **String** | This property is the discriminator for deciding between the specific types in the polymorphic chain of types. | [optional] 
**operation** | **String** | The operation name. | [optional] 
**startTime** | **Date** | The start time. | [optional] 
**status** | **String** | The job status. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)




