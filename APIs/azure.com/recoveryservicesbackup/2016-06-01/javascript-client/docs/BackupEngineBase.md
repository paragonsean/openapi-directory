# RecoveryServicesBackupClient.BackupEngineBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupEngineId** | **String** | The ID of the backup engine. | [optional] 
**backupEngineType** | **String** | The type of the backup engine. | [optional] 
**backupManagementType** | **String** | The type of backup management associated with the backup engine. | [optional] 
**canReRegister** | **Boolean** | The flag indicating whether the backup engine be registered again, once the engine has been initially registered. | [optional] 
**friendlyName** | **String** | The friendly name of the backup engine. | [optional] 
**healthStatus** | **String** | The backup status of the backup engine. | [optional] 
**registrationStatus** | **String** | The status of the backup engine registration with the Recovery Services vault. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)




