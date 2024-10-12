# RecoveryServicesBackupClient.JobQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Type of backup management for the job. | [optional] 
**endTime** | **Date** | The time when the job ends. The value is in UTC. | [optional] 
**jobId** | **String** | The ID of the job. Each jobID is unique. | [optional] 
**operation** | **String** | The type of operation. | [optional] 
**startTime** | **Date** | The time when the job starts. The value is in UTC. | [optional] 
**status** | **String** | Status of the job. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)





## Enum: OperationEnum


* `Invalid` (value: `"Invalid"`)

* `ConfigureBackup` (value: `"ConfigureBackup"`)

* `Backup` (value: `"Backup"`)

* `Restore` (value: `"Restore"`)

* `DisableBackup` (value: `"DisableBackup"`)

* `DeleteBackupData` (value: `"DeleteBackupData"`)





## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)

* `CompletedWithWarnings` (value: `"CompletedWithWarnings"`)

* `Cancelled` (value: `"Cancelled"`)

* `Cancelling` (value: `"Cancelling"`)




