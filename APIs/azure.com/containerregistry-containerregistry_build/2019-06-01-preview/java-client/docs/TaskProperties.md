

# TaskProperties

The properties of a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  |  [optional] |
|**creationDate** | **OffsetDateTime** | The creation date of task. |  [optional] [readonly] |
|**credentials** | [**Credentials**](Credentials.md) |  |  [optional] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the task. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of task. |  [optional] |
|**step** | [**TaskStepProperties**](TaskStepProperties.md) |  |  |
|**timeout** | **Integer** | Run timeout in seconds. |  [optional] |
|**trigger** | [**TriggerProperties**](TriggerProperties.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



