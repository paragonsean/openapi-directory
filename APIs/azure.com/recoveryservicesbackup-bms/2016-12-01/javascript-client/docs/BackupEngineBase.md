# RecoveryServicesBackupClient.BackupEngineBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureBackupAgentVersion** | **String** | Backup agent version | [optional] 
**backupEngineId** | **String** | ID of the backup engine. | [optional] 
**backupEngineState** | **String** | Status of the backup engine with the Recovery Services Vault. &#x3D; {Active/Deleting/DeleteFailed} | [optional] 
**backupEngineType** | **String** | Type of the backup engine. | [optional] 
**backupManagementType** | **String** | Type of backup management for the backup engine. | [optional] 
**canReRegister** | **Boolean** | Flag indicating if the backup engine be registered, once already registered. | [optional] 
**dpmVersion** | **String** | Backup engine version | [optional] 
**extendedInfo** | [**BackupEngineExtendedInfo**](BackupEngineExtendedInfo.md) |  | [optional] 
**friendlyName** | **String** | Friendly name of the backup engine. | [optional] 
**healthStatus** | **String** | Backup status of the backup engine. | [optional] 
**isAzureBackupAgentUpgradeAvailable** | **Boolean** | To check if backup agent upgrade available | [optional] 
**isDpmUpgradeAvailable** | **Boolean** | To check if backup engine upgrade available | [optional] 
**registrationStatus** | **String** | Registration status of the backup engine with the Recovery Services Vault. | [optional] 



## Enum: BackupEngineTypeEnum


* `Invalid` (value: `"Invalid"`)

* `DpmBackupEngine` (value: `"DpmBackupEngine"`)

* `AzureBackupServerEngine` (value: `"AzureBackupServerEngine"`)





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




