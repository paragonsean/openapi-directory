

# BackupEngineBase

The base backup engine class. All workload specific backup engines derive from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureBackupAgentVersion** | **String** | Backup agent version |  [optional] |
|**backupEngineId** | **String** | ID of the backup engine. |  [optional] |
|**backupEngineState** | **String** | Status of the backup engine with the Recovery Services Vault. &#x3D; {Active/Deleting/DeleteFailed} |  [optional] |
|**backupEngineType** | [**BackupEngineTypeEnum**](#BackupEngineTypeEnum) | Type of the backup engine. |  [optional] |
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Type of backup management for the backup engine. |  [optional] |
|**canReRegister** | **Boolean** | Flag indicating if the backup engine be registered, once already registered. |  [optional] |
|**dpmVersion** | **String** | Backup engine version |  [optional] |
|**extendedInfo** | [**BackupEngineExtendedInfo**](BackupEngineExtendedInfo.md) |  |  [optional] |
|**friendlyName** | **String** | Friendly name of the backup engine. |  [optional] |
|**healthStatus** | **String** | Backup status of the backup engine. |  [optional] |
|**isAzureBackupAgentUpgradeAvailable** | **Boolean** | To check if backup agent upgrade available |  [optional] |
|**isDpmUpgradeAvailable** | **Boolean** | To check if backup engine upgrade available |  [optional] |
|**registrationStatus** | **String** | Registration status of the backup engine with the Recovery Services Vault. |  [optional] |



## Enum: BackupEngineTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| DPM_BACKUP_ENGINE | &quot;DpmBackupEngine&quot; |
| AZURE_BACKUP_SERVER_ENGINE | &quot;AzureBackupServerEngine&quot; |



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



