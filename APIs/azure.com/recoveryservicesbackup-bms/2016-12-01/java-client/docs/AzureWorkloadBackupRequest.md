

# AzureWorkloadBackupRequest

AzureWorkload workload-specific backup request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupType** | [**BackupTypeEnum**](#BackupTypeEnum) | Type of backup, viz. Full, Differential, Log or CopyOnlyFull |  [optional] |
|**enableCompression** | **Boolean** | Bool for Compression setting |  [optional] |
|**recoveryPointExpiryTimeInUTC** | **OffsetDateTime** | Backup copy will expire after the time specified (UTC). |  [optional] |



## Enum: BackupTypeEnum

| Name | Value |
|---- | -----|
| INVALID | &quot;Invalid&quot; |
| FULL | &quot;Full&quot; |
| DIFFERENTIAL | &quot;Differential&quot; |
| LOG | &quot;Log&quot; |
| COPY_ONLY_FULL | &quot;CopyOnlyFull&quot; |



