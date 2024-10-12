# RecoveryServicesBackupClient.BackupStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poLogicalName** | **String** | Protectable Item Logical Name | [optional] 
**resourceId** | **String** | Entire ARM resource id of the resource | [optional] 
**resourceType** | **String** | Container Type - VM, SQLPaaS, DPM, AzureFileShare... | [optional] 



## Enum: ResourceTypeEnum


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




