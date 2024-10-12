

# TaskPropertiesUpdateParameters

The properties for updating a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  |  [optional] |
|**credentials** | [**Credentials**](Credentials.md) |  |  [optional] |
|**platform** | [**PlatformUpdateParameters**](PlatformUpdateParameters.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of task. |  [optional] |
|**step** | [**TaskStepUpdateParameters**](TaskStepUpdateParameters.md) |  |  [optional] |
|**timeout** | **Integer** | Run timeout in seconds. |  [optional] |
|**trigger** | [**TriggerUpdateParameters**](TriggerUpdateParameters.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



