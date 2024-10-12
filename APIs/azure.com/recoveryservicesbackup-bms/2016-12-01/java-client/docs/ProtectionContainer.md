

# ProtectionContainer

Base class for container with backup items. Containers with specific workloads are derived from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Type of backup management for the container. |  [optional] |
|**containerType** | [**ContainerTypeEnum**](#ContainerTypeEnum) | Type of the container. The value of this property for: 1. Compute Azure VM is Microsoft.Compute/virtualMachines 2.  Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines 3. Windows machines (like MAB, DPM etc) is  Windows 4. Azure SQL instance is AzureSqlContainer. 5. Storage containers is StorageContainer. 6. Azure workload  Backup is VMAppContainer |  [optional] |
|**friendlyName** | **String** | Friendly name of the container. |  [optional] |
|**healthStatus** | **String** | Status of health of the container. |  [optional] |
|**registrationStatus** | **String** | Status of registration of the container with the Recovery Services Vault. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |
| AZURE_STORAGE | &quot;AzureStorage&quot; |
| AZURE_WORKLOAD | &quot;AzureWorkload&quot; |
| DEFAULT_BACKUP | &quot;DefaultBackup&quot; |



## Enum: ContainerTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| UNKNOWN | &quot;Unknown&quot; |
| IAAS_VM_CONTAINER | &quot;IaasVMContainer&quot; |
| IAAS_VM_SERVICE_CONTAINER | &quot;IaasVMServiceContainer&quot; |
| DPM_CONTAINER | &quot;DPMContainer&quot; |
| AZURE_BACKUP_SERVER_CONTAINER | &quot;AzureBackupServerContainer&quot; |
| MAB_CONTAINER | &quot;MABContainer&quot; |
| CLUSTER | &quot;Cluster&quot; |
| AZURE_SQL_CONTAINER | &quot;AzureSqlContainer&quot; |
| WINDOWS | &quot;Windows&quot; |
| V_CENTER | &quot;VCenter&quot; |
| VM_APP_CONTAINER | &quot;VMAppContainer&quot; |
| SQLAG_WORK_LOAD_CONTAINER | &quot;SQLAGWorkLoadContainer&quot; |
| STORAGE_CONTAINER | &quot;StorageContainer&quot; |
| GENERIC_CONTAINER | &quot;GenericContainer&quot; |



