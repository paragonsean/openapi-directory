# BatchManagement.ContainerConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerImageNames** | **[String]** | This is the full image reference, as would be specified to \&quot;docker pull\&quot;. An image will be sourced from the default Docker registry unless the image is fully qualified with an alternative registry. | [optional] 
**containerRegistries** | [**[ContainerRegistry]**](ContainerRegistry.md) | If any images must be downloaded from a private registry which requires credentials, then those credentials must be provided here. | [optional] 
**type** | **String** |  | 



## Enum: TypeEnum


* `DockerCompatible` (value: `"DockerCompatible"`)




