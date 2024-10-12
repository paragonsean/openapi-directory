# StorSimpleManagementClient.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupPointInTime** | **Date** | The time of the backup used for the failover. | [optional] 
**deviceId** | **String** | The device id in which the job is currently running | [optional] 
**downloadProgress** | [**UpdateDownloadProgress**](UpdateDownloadProgress.md) |  | [optional] 
**entityId** | **String** | The entity identifier for which the job ran. | [optional] 
**entityType** | **String** | The entity type for which the job ran. | [optional] 
**installProgress** | [**UpdateInstallProgress**](UpdateInstallProgress.md) |  | [optional] 
**isCancellable** | **Boolean** | Represents whether the job is cancellable or not | [optional] 
**jobStages** | [**[JobStage]**](JobStage.md) | The job stages. | [optional] 
**jobType** | **String** | Type of the job | 
**sourceDeviceId** | **String** | The source device identifier of the failover job. | [optional] 
**stats** | [**JobStats**](JobStats.md) |  | [optional] 
**targetId** | **String** | Id of the object that is created by the job | [optional] 
**targetType** | **String** | The target type of the backup. | [optional] 



## Enum: JobTypeEnum


* `Backup` (value: `"Backup"`)

* `Clone` (value: `"Clone"`)

* `Failover` (value: `"Failover"`)

* `DownloadUpdates` (value: `"DownloadUpdates"`)

* `InstallUpdates` (value: `"InstallUpdates"`)





## Enum: TargetTypeEnum


* `FileServer` (value: `"FileServer"`)

* `DiskServer` (value: `"DiskServer"`)




