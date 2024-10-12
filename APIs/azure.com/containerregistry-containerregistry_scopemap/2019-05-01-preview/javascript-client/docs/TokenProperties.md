# ContainerRegistryManagementClient.TokenProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **Date** | The creation date of scope map. | [optional] [readonly] 
**credentials** | [**TokenCredentialsProperties**](TokenCredentialsProperties.md) |  | [optional] 
**objectId** | **String** | The user/group/application object ID for which the token has to be created. | [optional] 
**provisioningState** | **String** | Provisioning state of the resource. | [optional] [readonly] 
**scopeMapId** | **String** | The resource ID of the scope map to which the token will be associated with. | [optional] 
**status** | **String** | The status of the token example enabled or disabled. | [optional] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




