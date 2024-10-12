

# BMSContainerQueryObject

The query filters that can be used with the list containers API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupEngineName** | **String** | Backup engine name |  [optional] |
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Backup management type for this container. |  |
|**containerType** | [**ContainerTypeEnum**](#ContainerTypeEnum) | Type of container for filter |  [optional] |
|**fabricName** | **String** | Fabric name for filter |  [optional] |
|**friendlyName** | **String** | Friendly name of this container. |  [optional] |
|**status** | **String** | Status of registration of this container with the Recovery Services Vault. |  [optional] |



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



