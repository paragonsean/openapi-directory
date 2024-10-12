# RecoveryServicesBackupClient.MabContainerExtendedInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupItemType** | **String** | Type of backup items associated with this container. | [optional] 
**backupItems** | **[String]** | List of backup items associated with this container. | [optional] 
**lastBackupStatus** | **String** | Latest backup status of this container. | [optional] 
**lastRefreshedAt** | **Date** | Time stamp when this container was refreshed. | [optional] 
**policyName** | **String** | Backup policy associated with this container. | [optional] 



## Enum: BackupItemTypeEnum


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




