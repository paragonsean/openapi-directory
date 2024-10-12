# BackupForGkeApi.VolumeRestore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completeTime** | **String** | Output only. The timestamp when the associated underlying volume restoration completed. | [optional] [readonly] 
**createTime** | **String** | Output only. The timestamp when this VolumeRestore resource was created. | [optional] [readonly] 
**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume restore from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform volume restore updates in order to avoid race conditions. | [optional] [readonly] 
**name** | **String** | Output only. Full name of the VolumeRestore resource. Format: &#x60;projects/_*_/locations/_*_/restorePlans/_*_/restores/_*_/volumeRestores/_*&#x60; | [optional] [readonly] 
**state** | **String** | Output only. The current state of this VolumeRestore. | [optional] [readonly] 
**stateMessage** | **String** | Output only. A human readable message explaining why the VolumeRestore is in its current state. | [optional] [readonly] 
**targetPvc** | [**NamespacedName**](NamespacedName.md) |  | [optional] 
**uid** | **String** | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when this VolumeRestore resource was last updated. | [optional] [readonly] 
**volumeBackup** | **String** | Output only. The full name of the VolumeBackup from which the volume will be restored. Format: &#x60;projects/_*_/locations/_*_/backupPlans/_*_/backups/_*_/volumeBackups/_*&#x60;. | [optional] [readonly] 
**volumeHandle** | **String** | Output only. A storage system-specific opaque handler to the underlying volume created for the target PVC from the volume backup. | [optional] [readonly] 
**volumeType** | **String** | Output only. The type of volume provisioned | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `RESTORING` (value: `"RESTORING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)





## Enum: VolumeTypeEnum


* `VOLUME_TYPE_UNSPECIFIED` (value: `"VOLUME_TYPE_UNSPECIFIED"`)

* `GCE_PERSISTENT_DISK` (value: `"GCE_PERSISTENT_DISK"`)




