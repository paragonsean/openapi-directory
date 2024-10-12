# BackupForGkeApi.VolumeBackup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completeTime** | **String** | Output only. The timestamp when the associated underlying volume backup operation completed. | [optional] [readonly] 
**createTime** | **String** | Output only. The timestamp when this VolumeBackup resource was created. | [optional] [readonly] 
**diskSizeBytes** | **String** | Output only. The minimum size of the disk to which this VolumeBackup can be restored. | [optional] [readonly] 
**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume backup from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform volume backup updates in order to avoid race conditions. | [optional] [readonly] 
**format** | **String** | Output only. The format used for the volume backup. | [optional] [readonly] 
**name** | **String** | Output only. The full name of the VolumeBackup resource. Format: &#x60;projects/_*_/locations/_*_/backupPlans/_*_/backups/_*_/volumeBackups/_*&#x60;. | [optional] [readonly] 
**sourcePvc** | [**NamespacedName**](NamespacedName.md) |  | [optional] 
**state** | **String** | Output only. The current state of this VolumeBackup. | [optional] [readonly] 
**stateMessage** | **String** | Output only. A human readable message explaining why the VolumeBackup is in its current state. | [optional] [readonly] 
**storageBytes** | **String** | Output only. The aggregate size of the underlying artifacts associated with this VolumeBackup in the backup storage. This may change over time when multiple backups of the same volume share the same backup storage location. In particular, this is likely to increase in size when the immediately preceding backup of the same volume is deleted. | [optional] [readonly] 
**uid** | **String** | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when this VolumeBackup resource was last updated. | [optional] [readonly] 
**volumeBackupHandle** | **String** | Output only. A storage system-specific opaque handle to the underlying volume backup. | [optional] [readonly] 



## Enum: FormatEnum


* `VOLUME_BACKUP_FORMAT_UNSPECIFIED` (value: `"VOLUME_BACKUP_FORMAT_UNSPECIFIED"`)

* `GCE_PERSISTENT_DISK` (value: `"GCE_PERSISTENT_DISK"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `SNAPSHOTTING` (value: `"SNAPSHOTTING"`)

* `UPLOADING` (value: `"UPLOADING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)




