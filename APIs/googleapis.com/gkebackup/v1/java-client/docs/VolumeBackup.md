

# VolumeBackup

Represents the backup of a specific persistent volume as a component of a Backup - both the record of the operation and a pointer to the underlying storage-specific artifacts. Next id: 14

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completeTime** | **String** | Output only. The timestamp when the associated underlying volume backup operation completed. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The timestamp when this VolumeBackup resource was created. |  [optional] [readonly] |
|**diskSizeBytes** | **String** | Output only. The minimum size of the disk to which this VolumeBackup can be restored. |  [optional] [readonly] |
|**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume backup from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform volume backup updates in order to avoid race conditions. |  [optional] [readonly] |
|**format** | [**FormatEnum**](#FormatEnum) | Output only. The format used for the volume backup. |  [optional] [readonly] |
|**name** | **String** | Output only. The full name of the VolumeBackup resource. Format: &#x60;projects/_*_/locations/_*_/backupPlans/_*_/backups/_*_/volumeBackups/_*&#x60;. |  [optional] [readonly] |
|**sourcePvc** | [**NamespacedName**](NamespacedName.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of this VolumeBackup. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. A human readable message explaining why the VolumeBackup is in its current state. |  [optional] [readonly] |
|**storageBytes** | **String** | Output only. The aggregate size of the underlying artifacts associated with this VolumeBackup in the backup storage. This may change over time when multiple backups of the same volume share the same backup storage location. In particular, this is likely to increase in size when the immediately preceding backup of the same volume is deleted. |  [optional] [readonly] |
|**uid** | **String** | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when this VolumeBackup resource was last updated. |  [optional] [readonly] |
|**volumeBackupHandle** | **String** | Output only. A storage system-specific opaque handle to the underlying volume backup. |  [optional] [readonly] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| VOLUME_BACKUP_FORMAT_UNSPECIFIED | &quot;VOLUME_BACKUP_FORMAT_UNSPECIFIED&quot; |
| GCE_PERSISTENT_DISK | &quot;GCE_PERSISTENT_DISK&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| SNAPSHOTTING | &quot;SNAPSHOTTING&quot; |
| UPLOADING | &quot;UPLOADING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |



