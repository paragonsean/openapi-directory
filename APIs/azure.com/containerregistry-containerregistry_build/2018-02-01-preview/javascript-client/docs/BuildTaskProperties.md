# ContainerRegistryManagementClient.BuildTaskProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | The alternative updatable name for a build task. | 
**creationDate** | **Date** | The creation date of build task. | [optional] [readonly] 
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | 
**provisioningState** | **String** | The provisioning state of the build task. | [optional] [readonly] 
**sourceRepository** | [**SourceRepositoryProperties**](SourceRepositoryProperties.md) |  | 
**status** | **String** | The current status of build task. | [optional] 
**timeout** | **Number** | Build timeout in seconds. | [optional] [default to 3600]



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





## Enum: StatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




