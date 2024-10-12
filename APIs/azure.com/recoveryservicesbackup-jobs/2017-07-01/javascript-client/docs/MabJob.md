# RecoveryServicesBackupClient.MabJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | The state/actions applicable on jobs like cancel/retry. | [optional] 
**duration** | **String** | Time taken by job to run. | [optional] 
**errorDetails** | [**[MabErrorInfo]**](MabErrorInfo.md) | The errors. | [optional] 
**extendedInfo** | [**MabJobExtendedInfo**](MabJobExtendedInfo.md) |  | [optional] 
**mabServerName** | **String** | Name of server protecting the DS. | [optional] 
**mabServerType** | **String** | Server type of MAB container. | [optional] 
**workloadType** | **String** | Workload type of backup item. | [optional] 



## Enum: [ActionsInfoEnum]


* `Invalid` (value: `"Invalid"`)

* `Cancellable` (value: `"Cancellable"`)

* `Retriable` (value: `"Retriable"`)





## Enum: MabServerTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Unknown` (value: `"Unknown"`)

* `IaasVMContainer` (value: `"IaasVMContainer"`)

* `IaasVMServiceContainer` (value: `"IaasVMServiceContainer"`)

* `DPMContainer` (value: `"DPMContainer"`)

* `AzureBackupServerContainer` (value: `"AzureBackupServerContainer"`)

* `MABContainer` (value: `"MABContainer"`)

* `Cluster` (value: `"Cluster"`)

* `AzureSqlContainer` (value: `"AzureSqlContainer"`)

* `Windows` (value: `"Windows"`)

* `VCenter` (value: `"VCenter"`)





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




