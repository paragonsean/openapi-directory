

# ProtectionContainer

The base class for a container with backup items. Containers with specific workloads are derived from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | The backup management type for the container. |  [optional] |
|**containerType** | **String** | The type assigned to the container. The values to use for each of these properties are:&lt;br/&gt; 1. Compute Azure VM is Microsoft.Compute/virtualMachines&lt;br/&gt; 2. Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines&lt;br/&gt; 3. Windows machines (like Azure Backup Server and DPM) is Windows&lt;br/&gt; 4. Azure SQL instance is AzureSqlContainer. |  [optional] [readonly] |
|**friendlyName** | **String** | Friendly name of the container. |  [optional] |
|**healthStatus** | **String** | The status of the container&#39;s health. |  [optional] |
|**protectableObjectType** | **String** | The protectable object type associated with the container. |  [optional] |
|**registrationStatus** | **String** | The container&#39;s registration status with the Recovery Services vault. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |



