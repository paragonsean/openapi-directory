# ContainerRegistryManagementClient.ScopeMapProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **[String]** | The list of scoped permissions for registry artifacts.  E.g. repositories/repository-name/content/read,  repositories/repository-name/metadata/write | 
**creationDate** | **Date** | The creation date of scope map. | [optional] [readonly] 
**description** | **String** | The user friendly description of the scope map. | [optional] 
**provisioningState** | **String** | Provisioning state of the resource. | [optional] [readonly] 
**type** | **String** | The type of the scope map. E.g. BuildIn scope map. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




