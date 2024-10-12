# RecoveryServicesBackupClient.ProtectableContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | Type of backup management for the container. | [optional] 
**containerId** | **String** | Fabric Id of the container such as ARM Id. | [optional] 
**friendlyName** | **String** | Friendly name of the container. | [optional] 
**healthStatus** | **String** | Status of health of the container. | [optional] 
**protectableContainerType** | **String** | Type of the container. The value of this property for  1. Compute Azure VM is Microsoft.Compute/virtualMachines  2. Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines | [optional] [readonly] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)

* `AzureStorage` (value: `"AzureStorage"`)

* `AzureWorkload` (value: `"AzureWorkload"`)

* `DefaultBackup` (value: `"DefaultBackup"`)





## Enum: ProtectableContainerTypeEnum


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

* `VMAppContainer` (value: `"VMAppContainer"`)

* `SQLAGWorkLoadContainer` (value: `"SQLAGWorkLoadContainer"`)

* `StorageContainer` (value: `"StorageContainer"`)

* `GenericContainer` (value: `"GenericContainer"`)




