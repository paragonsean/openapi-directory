

# JobQueryObject

The filters to list the jobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Type of backup management for the job. |  [optional] |
|**endTime** | **OffsetDateTime** | The time when the job ends. The value is in UTC. |  [optional] |
|**jobId** | **String** | The ID of the job. Each jobID is unique. |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | The type of operation. |  [optional] |
|**startTime** | **OffsetDateTime** | The time when the job starts. The value is in UTC. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the job. |  [optional] |



## Enum: BackupManagementTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| AZURE_IAAS_VM | &quot;AzureIaasVM&quot; |
| MAB | &quot;MAB&quot; |
| DPM | &quot;DPM&quot; |
| AZURE_BACKUP_SERVER | &quot;AzureBackupServer&quot; |
| AZURE_SQL | &quot;AzureSql&quot; |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| CONFIGURE_BACKUP | &quot;ConfigureBackup&quot; |
| BACKUP | &quot;Backup&quot; |
| RESTORE | &quot;Restore&quot; |
| DISABLE_BACKUP | &quot;DisableBackup&quot; |
| DELETE_BACKUP_DATA | &quot;DeleteBackupData&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |
| COMPLETED_WITH_WARNINGS | &quot;CompletedWithWarnings&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CANCELLING | &quot;Cancelling&quot; |



