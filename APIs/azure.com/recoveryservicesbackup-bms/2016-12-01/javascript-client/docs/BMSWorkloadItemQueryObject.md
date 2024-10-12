# RecoveryServicesBackupClient.BMSWorkloadItemQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Backup management type. | [optional] 
**protectionStatus** | **String** | Backup status query parameter. | [optional] 
**workloadItemType** | **String** | Workload Item type | [optional] 
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





## Enum: ProtectionStatusEnum


* `Invalid` (value: `"Invalid"`)

* `NotProtected` (value: `"NotProtected"`)

* `Protecting` (value: `"Protecting"`)

* `Protected` (value: `"Protected"`)

* `ProtectionFailed` (value: `"ProtectionFailed"`)





## Enum: WorkloadItemTypeEnum


* `Invalid` (value: `"Invalid"`)

* `SQLInstance` (value: `"SQLInstance"`)

* `SQLDataBase` (value: `"SQLDataBase"`)

* `SAPHanaSystem` (value: `"SAPHanaSystem"`)

* `SAPHanaDatabase` (value: `"SAPHanaDatabase"`)

* `SAPAseSystem` (value: `"SAPAseSystem"`)

* `SAPAseDatabase` (value: `"SAPAseDatabase"`)





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




