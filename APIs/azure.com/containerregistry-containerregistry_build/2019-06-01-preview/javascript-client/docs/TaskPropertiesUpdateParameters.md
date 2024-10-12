# ContainerRegistryManagementClient.TaskPropertiesUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**platform** | [**PlatformUpdateParameters**](PlatformUpdateParameters.md) |  | [optional] 
**status** | **String** | The current status of task. | [optional] 
**step** | [**TaskStepUpdateParameters**](TaskStepUpdateParameters.md) |  | [optional] 
**timeout** | **Number** | Run timeout in seconds. | [optional] 
**trigger** | [**TriggerUpdateParameters**](TriggerUpdateParameters.md) |  | [optional] 



## Enum: StatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




