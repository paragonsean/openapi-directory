# RecoveryServicesBackupClient.ProtectedItemQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupEngineName** | **String** | Backup Engine name | [optional] 
**backupManagementType** | **String** | Backup management type for the backed up item. | [optional] 
**backupSetName** | **String** | Name of the backup set. | [optional] 
**containerName** | **String** | Name of the container. | [optional] 
**fabricName** | **String** | Name of the fabric. | [optional] 
**friendlyName** | **String** | Friendly name of protected item | [optional] 
**healthState** | **String** | Health State for the backed up item. | [optional] 
**itemType** | **String** | Type of workload this item represents. | [optional] 
**policyName** | **String** | Backup policy name associated with the backup item. | [optional] 



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





## Enum: HealthStateEnum


* `Passed` (value: `"Passed"`)

* `ActionRequired` (value: `"ActionRequired"`)

* `ActionSuggested` (value: `"ActionSuggested"`)

* `Invalid` (value: `"Invalid"`)





## Enum: ItemTypeEnum


* `Invalid` (value: `"Invalid"`)

* `VM` (value: `"VM"`)

* `FileFolder` (value: `"FileFolder"`)

* `AzureSqlDb` (value: `"AzureSqlDb"`)

* `SQLDB` (value: `"SQLDB"`)

* `Exchange` (value: `"Exchange"`)

* `Sharepoint` (value: `"Sharepoint"`)

* `VMwareVM` (value: `"VMwareVM"`)

* `SystemState` (value: `"SystemState"`)

* `Client` (value: `"Client"`)

* `GenericDataSource` (value: `"GenericDataSource"`)

* `SQLDataBase` (value: `"SQLDataBase"`)

* `AzureFileShare` (value: `"AzureFileShare"`)

* `SAPHanaDatabase` (value: `"SAPHanaDatabase"`)

* `SAPAseDatabase` (value: `"SAPAseDatabase"`)




