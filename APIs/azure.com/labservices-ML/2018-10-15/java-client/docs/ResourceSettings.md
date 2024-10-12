

# ResourceSettings

Represents resource specific settings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cores** | **Integer** | The translated compute cores of the virtual machine |  [optional] [readonly] |
|**galleryImageResourceId** | **String** | The resource id of the gallery image used for creating the virtual machine |  [optional] |
|**id** | **String** | The unique id of the resource setting |  [optional] [readonly] |
|**imageName** | **String** | The name of the image used to created the environment setting |  [optional] [readonly] |
|**referenceVm** | [**ReferenceVm**](ReferenceVm.md) |  |  |
|**size** | [**SizeEnum**](#SizeEnum) | The size of the virtual machine |  [optional] |



## Enum: SizeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| STANDARD | &quot;Standard&quot; |
| PERFORMANCE | &quot;Performance&quot; |



