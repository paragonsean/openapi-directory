

# SecondaryBootDisk

SecondaryBootDisk represents a persistent disk attached to a node with special configurations based on its mode.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskImage** | **String** | Fully-qualified resource ID for an existing disk image. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Disk mode (container image cache, etc.) |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| CONTAINER_IMAGE_CACHE | &quot;CONTAINER_IMAGE_CACHE&quot; |



