# RecoveryServicesBackupClient.AzureWorkloadBackupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupType** | **String** | Type of backup, viz. Full, Differential, Log or CopyOnlyFull | [optional] 
**enableCompression** | **Boolean** | Bool for Compression setting | [optional] 
**recoveryPointExpiryTimeInUTC** | **Date** | Backup copy will expire after the time specified (UTC). | [optional] 



## Enum: BackupTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Full` (value: `"Full"`)

* `Differential` (value: `"Differential"`)

* `Log` (value: `"Log"`)

* `CopyOnlyFull` (value: `"CopyOnlyFull"`)




