

# Job

Defines workload-agnostic properties for a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityId** | **String** | ActivityId of job. |  [optional] |
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | The backup management type for the current job. |  [optional] |
|**endTime** | **OffsetDateTime** | The end time. |  [optional] |
|**entityFriendlyName** | **String** | The friendly name of the entity on which the current job is executing. |  [optional] |
|**jobType** | **String** | This property is the discriminator for deciding between the specific types in the polymorphic chain of types. |  [optional] |
|**operation** | **String** | The operation name. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time. |  [optional] |
|**status** | **String** | The job status. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |



