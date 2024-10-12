# RecoveryServicesBackupClient.BMSContainerQueryObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupEngineName** | **String** | Backup engine name | [optional] 
**backupManagementType** | **String** | Backup management type for this container. | 
**containerType** | **String** | Type of container for filter | [optional] 
**fabricName** | **String** | Fabric name for filter | [optional] 
**friendlyName** | **String** | Friendly name of this container. | [optional] 
**status** | **String** | Status of registration of this container with the Recovery Services Vault. | [optional] 



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





## Enum: ContainerTypeEnum


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




