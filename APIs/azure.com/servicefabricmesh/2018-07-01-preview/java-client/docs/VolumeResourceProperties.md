

# VolumeResourceProperties

Describes properties of a volume resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | **String** | State of the resource. |  [optional] [readonly] |
|**azureFileParameters** | [**VolumeProviderParametersAzureFile**](VolumeProviderParametersAzureFile.md) |  |  [optional] |
|**description** | **String** | User readable description of the volume. |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | Provider of the volume. |  |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| SF_AZURE_FILE | &quot;SFAzureFile&quot; |



