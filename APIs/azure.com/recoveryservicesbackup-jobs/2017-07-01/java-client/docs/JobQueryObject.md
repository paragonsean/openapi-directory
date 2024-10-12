

# JobQueryObject

Filters to list the jobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupManagementType** | [**BackupManagementTypeEnum**](#BackupManagementTypeEnum) | Type of backup managmenent for the job. |  [optional] |
|**endTime** | **OffsetDateTime** | Job has ended at this time. Value is in UTC. |  [optional] |
|**jobId** | **String** | JobID represents the job uniquely. |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | Type of operation. |  [optional] |
|**startTime** | **OffsetDateTime** | Job has started at this time. Value is in UTC. |  [optional] |
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
| REGISTER | &quot;Register&quot; |
| UN_REGISTER | &quot;UnRegister&quot; |
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



