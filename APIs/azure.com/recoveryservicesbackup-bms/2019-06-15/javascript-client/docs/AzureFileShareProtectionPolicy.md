# RecoveryServicesBackupClient.AzureFileShareProtectionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retentionPolicy** | [**RetentionPolicy**](RetentionPolicy.md) |  | [optional] 
**schedulePolicy** | [**SchedulePolicy**](SchedulePolicy.md) |  | [optional] 
**timeZone** | **String** | TimeZone optional input as string. For example: TimeZone &#x3D; \&quot;Pacific Standard Time\&quot;. | [optional] 
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




