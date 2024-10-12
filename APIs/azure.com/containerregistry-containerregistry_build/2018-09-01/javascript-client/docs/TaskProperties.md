# ContainerRegistryManagementClient.TaskProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  | [optional] 
**creationDate** | **Date** | The creation date of task. | [optional] [readonly] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | 
**provisioningState** | **String** | The provisioning state of the task. | [optional] [readonly] 
**status** | **String** | The current status of task. | [optional] 
**step** | [**TaskStepProperties**](TaskStepProperties.md) |  | 
**timeout** | **Number** | Run timeout in seconds. | [optional] [default to 3600]
**trigger** | [**TriggerProperties**](TriggerProperties.md) |  | [optional] 



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




