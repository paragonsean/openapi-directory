# StorSimple8000SeriesManagementClient.VolumeProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessControlRecordIds** | **[String]** | The IDs of the access control records, associated with the volume. | 
**backupPolicyIds** | **[String]** | The IDs of the backup policies, in which this volume is part of. | [optional] [readonly] 
**backupStatus** | **String** | The backup status of the volume. | [optional] [readonly] 
**monitoringStatus** | **String** | The monitoring status of the volume. | 
**operationStatus** | **String** | The operation status on the volume. | [optional] [readonly] 
**sizeInBytes** | **Number** | The size of the volume in bytes. | 
**volumeContainerId** | **String** | The ID of the volume container, in which this volume is created. | [optional] [readonly] 
**volumeStatus** | **String** | The volume status. | 
**volumeType** | **String** | The type of the volume. | 



## Enum: BackupStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: MonitoringStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: OperationStatusEnum


* `None` (value: `"None"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Restoring` (value: `"Restoring"`)





## Enum: VolumeStatusEnum


* `Online` (value: `"Online"`)

* `Offline` (value: `"Offline"`)





## Enum: VolumeTypeEnum


* `Tiered` (value: `"Tiered"`)

* `Archival` (value: `"Archival"`)

* `LocallyPinned` (value: `"LocallyPinned"`)




