# StorSimple8000SeriesManagementClient.VolumeFailoverMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupCreatedDate** | **Date** | The date at which the snapshot was taken. | [optional] 
**backupElementId** | **String** | The path ID of the backup-element for this volume, inside the backup set. | [optional] 
**backupId** | **String** | The path ID of the backup set. | [optional] 
**backupPolicyId** | **String** | The path ID of the backup policy using which the snapshot was taken. | [optional] 
**sizeInBytes** | **Number** | The size of the volume in bytes at the time the snapshot was taken. | [optional] 
**volumeId** | **String** | The path ID of the volume. | [optional] 
**volumeType** | **String** | The type of the volume. | [optional] 



## Enum: VolumeTypeEnum


* `Tiered` (value: `"Tiered"`)

* `Archival` (value: `"Archival"`)

* `LocallyPinned` (value: `"LocallyPinned"`)




