# RecoveryServicesBackupClient.BMSPOQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Backup management type. | [optional] 
**containerName** | **String** | Full name of the container whose Protectable Objects should be returned. | [optional] 
**friendlyName** | **String** | Friendly name. | [optional] 
**status** | **String** | Backup status query parameter. | [optional] 
**workloadType** | **String** | Workload type | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureSql` (value: `"AzureSql"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureWorkload` (value: `"AzureWorkload"`)

* `AzureStorage` (value: `"AzureStorage"`)

* `DefaultBackup` (value: `"DefaultBackup"`)





## Enum: WorkloadTypeEnum


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




