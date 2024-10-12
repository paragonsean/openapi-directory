# RecoveryServicesBackupClient.AzureVmWorkloadProtectionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**makePolicyConsistent** | **Boolean** | Fix the policy inconsistency | [optional] 
**settings** | [**Settings**](Settings.md) |  | [optional] 
**subProtectionPolicy** | [**[SubProtectionPolicy]**](SubProtectionPolicy.md) | List of sub-protection policies which includes schedule and retention | [optional] 
**workLoadType** | **String** | Type of workload for the backup management | [optional] 



## Enum: WorkLoadTypeEnum


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




