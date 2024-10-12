

# BackupEngineBase

The base backup engine class. All workload-specific backup engines derive from this class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupEngineId** | **String** | The ID of the backup engine. |  [optional] |
|**backupEngineType** | **String** | The type of the backup engine. |  [optional] |
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | The type of backup management associated with the backup engine. |  [optional] |
|**canReRegister** | **Boolean** | The flag indicating whether the backup engine be registered again, once the engine has been initially registered. |  [optional] |
|**friendlyName** | **String** | The friendly name of the backup engine. |  [optional] |
|**healthStatus** | **String** | The backup status of the backup engine. |  [optional] |
|**registrationStatus** | **String** | The status of the backup engine registration with the Recovery Services vault. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |



