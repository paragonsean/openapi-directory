

# BMSRefreshContainersQueryObject

The query filters that can be used with the refresh container API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Backup management type for this container. |  [optional] |



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



