# RecoveryServicesBackupClient.MabJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionsInfo** | **[String]** | The state or actions applicable on jobs such as Cancel or Retry. | [optional] 
**duration** | **String** | The time required for the job to run. | [optional] 
**errorDetails** | [**[MabErrorInfo]**](MabErrorInfo.md) | The errors. | [optional] 
**extendedInfo** | [**MabJobExtendedInfo**](MabJobExtendedInfo.md) |  | [optional] 
**mabServerName** | **String** | The name of server protecting the data store. | [optional] 
**mabServerType** | **String** | Server type of the Azure Backup Server container. | [optional] 
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

* `DPMVenusContainer` (value: `"DPMVenusContainer"`)

* `MABContainer` (value: `"MABContainer"`)

* `ClusterResource` (value: `"ClusterResource"`)

* `AzureSqlContainer` (value: `"AzureSqlContainer"`)

* `WindowsServer` (value: `"WindowsServer"`)

* `Windows` (value: `"Windows"`)





## Enum: WorkloadTypeEnum


* `Invalid` (value: `"Invalid"`)

* `VM` (value: `"VM"`)

* `FileFolder` (value: `"FileFolder"`)

* `AzureSqlDb` (value: `"AzureSqlDb"`)

* `SQLDB` (value: `"SQLDB"`)

* `Exchange` (value: `"Exchange"`)

* `Sharepoint` (value: `"Sharepoint"`)

* `DPMUnknown` (value: `"DPMUnknown"`)




