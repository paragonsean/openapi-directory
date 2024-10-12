# RecoveryServicesBackupClient.PreValidateEnableBackupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **String** | Configuration of VM if any needs to be validated like OS type etc | [optional] 
**resourceId** | **String** | ARM Virtual Machine Id | [optional] 
**resourceType** | **String** | ProtectedItem Type- VM, SqlDataBase, AzureFileShare etc | [optional] 
**vaultId** | **String** | ARM id of the Recovery Services Vault | [optional] 



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




