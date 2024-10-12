# StorSimple8000SeriesManagementClient.JobProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupPointInTime** | **Date** | The time of the backup used for the failover. | [optional] 
**backupType** | **String** | The backup type (CloudSnapshot | LocalSnapshot). Applicable only for backup jobs. | [optional] 
**dataStats** | [**DataStatistics**](DataStatistics.md) |  | [optional] 
**deviceId** | **String** | The device ID in which the job ran. | [optional] 
**entityLabel** | **String** | The entity identifier for which the job ran. | [optional] 
**entityType** | **String** | The entity type for which the job ran. | [optional] 
**isCancellable** | **Boolean** | Represents whether the job is cancellable or not. | [optional] 
**jobStages** | [**[JobStage]**](JobStage.md) | The job stages. | [optional] 
**jobType** | **String** | The type of the job. | 
**sourceDeviceId** | **String** | The source device ID of the failover job. | [optional] 



## Enum: BackupTypeEnum


* `LocalSnapshot` (value: `"LocalSnapshot"`)

* `CloudSnapshot` (value: `"CloudSnapshot"`)





## Enum: JobTypeEnum


* `ScheduledBackup` (value: `"ScheduledBackup"`)

* `ManualBackup` (value: `"ManualBackup"`)

* `RestoreBackup` (value: `"RestoreBackup"`)

* `CloneVolume` (value: `"CloneVolume"`)

* `FailoverVolumeContainers` (value: `"FailoverVolumeContainers"`)

* `CreateLocallyPinnedVolume` (value: `"CreateLocallyPinnedVolume"`)

* `ModifyVolume` (value: `"ModifyVolume"`)

* `InstallUpdates` (value: `"InstallUpdates"`)

* `SupportPackageLogs` (value: `"SupportPackageLogs"`)

* `CreateCloudAppliance` (value: `"CreateCloudAppliance"`)




