# ContainerRegistryManagementClient.BuildTaskPropertiesUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | The alternative updatable name for a build task. | [optional] 
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | [optional] 
**sourceRepository** | [**SourceRepositoryUpdateParameters**](SourceRepositoryUpdateParameters.md) |  | [optional] 
**status** | **String** | The current status of build task. | [optional] 
**timeout** | **Number** | Build timeout in seconds. | [optional] 



## Enum: StatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




