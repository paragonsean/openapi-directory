# RecoveryServicesBackupClient.AzureWorkloadContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extendedInfo** | [**AzureWorkloadContainerExtendedInfo**](AzureWorkloadContainerExtendedInfo.md) |  | [optional] 
**lastUpdatedTime** | **Date** | Time stamp when this container was updated. | [optional] 
**operationType** | **String** | Re-Do Operation | [optional] 
**sourceResourceId** | **String** | ARM ID of the virtual machine represented by this Azure Workload Container | [optional] 
**workloadType** | **String** | Workload type for which registration was sent. | [optional] 



## Enum: OperationTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Register` (value: `"Register"`)

* `Reregister` (value: `"Reregister"`)





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




