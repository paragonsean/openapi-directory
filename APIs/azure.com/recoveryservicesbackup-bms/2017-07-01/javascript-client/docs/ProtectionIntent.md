# RecoveryServicesBackupClient.ProtectionIntent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Type of backup management for the backed up item. | [optional] 
**itemId** | **String** | ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId | [optional] 
**policyId** | **String** | ID of the backup policy with which this item is backed up. | [optional] 
**protectionIntentItemType** | **String** | backup protectionIntent type. | [optional] 
**protectionState** | **String** | Backup state of this backup item. | [optional] 
**sourceResourceId** | **String** | ARM ID of the resource to be backed up. | [optional] 



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





## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `NotProtected` (value: `"NotProtected"`)

* `Protecting` (value: `"Protecting"`)

* `Protected` (value: `"Protected"`)

* `ProtectionFailed` (value: `"ProtectionFailed"`)




