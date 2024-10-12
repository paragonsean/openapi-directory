# RecoveryServicesBackupClient.ProtectionIntentQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Backup management type for the backed up item | [optional] 
**itemName** | **String** | Item name of the intent | [optional] 
**itemType** | **String** | Type of workload this item represents | [optional] 
**parentName** | **String** | Parent name of the intent | [optional] 



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





## Enum: ItemTypeEnum


* `Invalid` (value: `"Invalid"`)

* `SQLInstance` (value: `"SQLInstance"`)

* `SQLAvailabilityGroupContainer` (value: `"SQLAvailabilityGroupContainer"`)




