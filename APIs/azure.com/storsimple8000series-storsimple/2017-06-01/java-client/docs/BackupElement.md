

# BackupElement

The backup element.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elementId** | **String** | The path ID that uniquely identifies the backup element. |  |
|**elementName** | **String** | The name of the backup element. |  |
|**elementType** | **String** | The hierarchical type of the backup element. |  |
|**sizeInBytes** | **Long** | The size in bytes. |  |
|**volumeContainerId** | **String** | The path ID of the volume container. |  |
|**volumeName** | **String** | The name of the volume. |  |
|**volumeType** | [**VolumeTypeEnum**](#VolumeTypeEnum) | The volume type. |  [optional] |



## Enum: VolumeTypeEnum

| Name | Value |
|---- | -----|
| TIERED | &quot;Tiered&quot; |
| ARCHIVAL | &quot;Archival&quot; |
| LOCALLY_PINNED | &quot;LocallyPinned&quot; |



