

# JobProperties

properties for the job

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupPointInTime** | **OffsetDateTime** | The time of the backup used for the failover. |  [optional] |
|**deviceId** | **String** | The device id in which the job is currently running |  [optional] |
|**downloadProgress** | [**UpdateDownloadProgress**](UpdateDownloadProgress.md) |  |  [optional] |
|**entityId** | **String** | The entity identifier for which the job ran. |  [optional] |
|**entityType** | **String** | The entity type for which the job ran. |  [optional] |
|**installProgress** | [**UpdateInstallProgress**](UpdateInstallProgress.md) |  |  [optional] |
|**isCancellable** | **Boolean** | Represents whether the job is cancellable or not |  [optional] |
|**jobStages** | [**List&lt;JobStage&gt;**](JobStage.md) | The job stages. |  [optional] |
|**jobType** | [**JobTypeEnum**](#JobTypeEnum) | Type of the job |  |
|**sourceDeviceId** | **String** | The source device identifier of the failover job. |  [optional] |
|**stats** | [**JobStats**](JobStats.md) |  |  [optional] |
|**targetId** | **String** | Id of the object that is created by the job |  [optional] |
|**targetType** | [**TargetTypeEnum**](#TargetTypeEnum) | The target type of the backup. |  [optional] |



## Enum: JobTypeEnum

| Name | Value |
|---- | -----|
| BACKUP | &quot;Backup&quot; |
| CLONE | &quot;Clone&quot; |
| FAILOVER | &quot;Failover&quot; |
| DOWNLOAD_UPDATES | &quot;DownloadUpdates&quot; |
| INSTALL_UPDATES | &quot;InstallUpdates&quot; |



## Enum: TargetTypeEnum

| Name | Value |
|---- | -----|
| FILE_SERVER | &quot;FileServer&quot; |
| DISK_SERVER | &quot;DiskServer&quot; |



