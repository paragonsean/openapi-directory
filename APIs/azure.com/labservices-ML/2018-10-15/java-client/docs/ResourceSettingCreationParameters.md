

# ResourceSettingCreationParameters

Represents resource specific settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**galleryImageResourceId** | **String** | The resource id of the gallery image used for creating the virtual machine |  |
|**location** | **String** | The location where the virtual machine will live |  [optional] |
|**name** | **String** | The name of the resource setting |  [optional] |
|**referenceVmCreationParameters** | [**ReferenceVmCreationParameters**](ReferenceVmCreationParameters.md) |  |  |
|**size** | [**SizeEnum**](#SizeEnum) | The size of the virtual machine |  [optional] |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PERFORMANCE | &quot;Performance&quot; |



