

# Job

Defines workload agnostic properties for a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityId** | **String** | ActivityId of job. |  [optional] |
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Backup management type to execute the current job. |  [optional] |
|**endTime** | **OffsetDateTime** | The end time. |  [optional] |
|**entityFriendlyName** | **String** | Friendly name of the entity on which the current job is executing. |  [optional] |
|**jobType** | **String** | This property will be used as the discriminator for deciding the specific types in the polymorhpic chain of types. |  |
|**operation** | **String** | The operation name. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time. |  [optional] |
|**status** | **String** | Job status. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |



