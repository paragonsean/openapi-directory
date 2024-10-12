# RecoveryServicesBackupClient.JobQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Type of backup management for the job. | [optional] 
**endTime** | **Date** | Job has ended at this time. Value is in UTC. | [optional] 
**jobId** | **String** | JobID represents the job uniquely. | [optional] 
**operation** | **String** | Type of operation. | [optional] 
**startTime** | **Date** | Job has started at this time. Value is in UTC. | [optional] 
**status** | **String** | Status of the job. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)

* `AzureStorage` (value: `"AzureStorage"`)

* `AzureWorkload` (value: `"AzureWorkload"`)

* `DefaultBackup` (value: `"DefaultBackup"`)





## Enum: OperationEnum


* `Invalid` (value: `"Invalid"`)

* `Register` (value: `"Register"`)

* `UnRegister` (value: `"UnRegister"`)

* `ConfigureBackup` (value: `"ConfigureBackup"`)

* `Backup` (value: `"Backup"`)

* `Restore` (value: `"Restore"`)

* `DisableBackup` (value: `"DisableBackup"`)

* `DeleteBackupData` (value: `"DeleteBackupData"`)

* `CrossRegionRestore` (value: `"CrossRegionRestore"`)

* `Undelete` (value: `"Undelete"`)





## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `InProgress` (value: `"InProgress"`)

* `Completed` (value: `"Completed"`)

* `Failed` (value: `"Failed"`)

* `CompletedWithWarnings` (value: `"CompletedWithWarnings"`)

* `Cancelled` (value: `"Cancelled"`)

* `Cancelling` (value: `"Cancelling"`)




