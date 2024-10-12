# RecoveryServicesBackupClient.ProtectionContainer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupManagementType** | **String** | The backup management type for the container. | [optional] 
**containerType** | **String** | The type assigned to the container. The values to use for each of these properties are:&lt;br/&gt; 1. Compute Azure VM is Microsoft.Compute/virtualMachines&lt;br/&gt; 2. Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines&lt;br/&gt; 3. Windows machines (like Azure Backup Server and DPM) is Windows&lt;br/&gt; 4. Azure SQL instance is AzureSqlContainer. | [optional] [readonly] 
**friendlyName** | **String** | Friendly name of the container. | [optional] 
**healthStatus** | **String** | The status of the container&#39;s health. | [optional] 
**protectableObjectType** | **String** | The protectable object type associated with the container. | [optional] 
**registrationStatus** | **String** | The container&#39;s registration status with the Recovery Services vault. | [optional] 



## Enum: BackupManagementTypeEnum


* `Invalid` (value: `"Invalid"`)

* `AzureIaasVM` (value: `"AzureIaasVM"`)

* `MAB` (value: `"MAB"`)

* `DPM` (value: `"DPM"`)

* `AzureBackupServer` (value: `"AzureBackupServer"`)

* `AzureSql` (value: `"AzureSql"`)




