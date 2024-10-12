

# JobProperties

The properties of the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupPointInTime** | **OffsetDateTime** | The time of the backup used for the failover. |  [optional] |
|**backupType** | [**BackupTypeEnum**](#BackupTypeEnum) | The backup type (CloudSnapshot | LocalSnapshot). Applicable only for backup jobs. |  [optional] |
|**dataStats** | [**DataStatistics**](DataStatistics.md) |  |  [optional] |
|**deviceId** | **String** | The device ID in which the job ran. |  [optional] |
|**entityLabel** | **String** | The entity identifier for which the job ran. |  [optional] |
|**entityType** | **String** | The entity type for which the job ran. |  [optional] |
|**isCancellable** | **Boolean** | Represents whether the job is cancellable or not. |  [optional] |
|**jobStages** | [**List&lt;JobStage&gt;**](JobStage.md) | The job stages. |  [optional] |
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | The type of the job. |  |
|**sourceDeviceId** | **String** | The source device ID of the failover job. |  [optional] |



## Enum: BackupTypeEnum

| Name | Value |
|---- | -----|
| LOCAL_SNAPSHOT | &quot;LocalSnapshot&quot; |
| CLOUD_SNAPSHOT | &quot;CloudSnapshot&quot; |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| SCHEDULED_BACKUP | &quot;ScheduledBackup&quot; |
| MANUAL_BACKUP | &quot;ManualBackup&quot; |
| RESTORE_BACKUP | &quot;RestoreBackup&quot; |
| CLONE_VOLUME | &quot;CloneVolume&quot; |
| FAILOVER_VOLUME_CONTAINERS | &quot;FailoverVolumeContainers&quot; |
| CREATE_LOCALLY_PINNED_VOLUME | &quot;CreateLocallyPinnedVolume&quot; |
| MODIFY_VOLUME | &quot;ModifyVolume&quot; |
| INSTALL_UPDATES | &quot;InstallUpdates&quot; |
| SUPPORT_PACKAGE_LOGS | &quot;SupportPackageLogs&quot; |
| CREATE_CLOUD_APPLIANCE | &quot;CreateCloudAppliance&quot; |



