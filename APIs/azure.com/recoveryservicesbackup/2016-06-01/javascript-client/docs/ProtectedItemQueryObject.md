# RecoveryServicesBackupClient.ProtectedItemQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | The backup management type associated with an item. | [optional] 
**containerName** | **String** | The name of the container. | [optional] 
**itemType** | **String** | The workload type associated with an item. | [optional] 
**policyName** | **String** | The name of the backup policy associated with the item. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)





## Enum: ItemTypeEnum


* `Invalid` (value: `"Invalid"`)

* `VM` (value: `"VM"`)

* `FileFolder` (value: `"FileFolder"`)

* `AzureSqlDb` (value: `"AzureSqlDb"`)

* `SQLDB` (value: `"SQLDB"`)

* `Exchange` (value: `"Exchange"`)

* `Sharepoint` (value: `"Sharepoint"`)

* `DPMUnknown` (value: `"DPMUnknown"`)




