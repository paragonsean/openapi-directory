# BatchService.ContainerConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerImageNames** | **[String]** | This is the full Image reference, as would be specified to \&quot;docker pull\&quot;. An Image will be sourced from the default Docker registry unless the Image is fully qualified with an alternative registry. | [optional] 
**containerRegistries** | [**[ContainerRegistry]**](ContainerRegistry.md) | If any Images must be downloaded from a private registry which requires credentials, then those credentials must be provided here. | [optional] 
**type** | **String** |  | 



## Enum: TypeEnum


* `dockerCompatible` (value: `"dockerCompatible"`)




