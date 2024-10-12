

# ContainerConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerImageNames** | **List&lt;String&gt;** | This is the full Image reference, as would be specified to \&quot;docker pull\&quot;. An Image will be sourced from the default Docker registry unless the Image is fully qualified with an alternative registry. |  [optional] |
|**containerRegistries** | [**List&lt;ContainerRegistry&gt;**](ContainerRegistry.md) | If any Images must be downloaded from a private registry which requires credentials, then those credentials must be provided here. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DOCKER_COMPATIBLE | &quot;dockerCompatible&quot; |



