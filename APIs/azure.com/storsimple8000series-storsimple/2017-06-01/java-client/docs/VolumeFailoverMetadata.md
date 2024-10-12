

# VolumeFailoverMetadata

The metadata of a volume that has valid cloud snapshot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupCreatedDate** | **OffsetDateTime** | The date at which the snapshot was taken. |  [optional] |
|**backupElementId** | **String** | The path ID of the backup-element for this volume, inside the backup set. |  [optional] |
|**backupId** | **String** | The path ID of the backup set. |  [optional] |
|**backupPolicyId** | **String** | The path ID of the backup policy using which the snapshot was taken. |  [optional] |
|**sizeInBytes** | **Long** | The size of the volume in bytes at the time the snapshot was taken. |  [optional] |
|**volumeId** | **String** | The path ID of the volume. |  [optional] |
|**volumeType** | [**VolumeTypeEnum**](#VolumeTypeEnum) | The type of the volume. |  [optional] |



## Enum: VolumeTypeEnum

| Name | Value |
|---- | -----|
| TIERED | &quot;Tiered&quot; |
| ARCHIVAL | &quot;Archival&quot; |
| LOCALLY_PINNED | &quot;LocallyPinned&quot; |



