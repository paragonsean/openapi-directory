

# VolumeResourceProperties

This type describes properties of a volume resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | State of the resource. |  [optional] [readonly] |
|**azureFileParameters** | [**VolumeProviderParametersAzureFile**](VolumeProviderParametersAzureFile.md) |  |  [optional] |
|**description** | **String** | User readable description of the volume. |  [optional] |
|**provider** | **VolumeProvider** |  |  |
|**status** | **ResourceStatus** |  |  [optional] |
|**statusDetails** | **String** | Gives additional information about the current status of the volume. |  [optional] [readonly] |



