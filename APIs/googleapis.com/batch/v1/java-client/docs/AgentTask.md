

# AgentTask

TODO(b/182501497) The message needs to be redefined when the Agent API server updates data in storage per the backend design.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentTaskSpec** | [**AgentTaskSpec**](AgentTaskSpec.md) |  |  [optional] |
|**intendedState** | [**IntendedStateEnum**](#IntendedStateEnum) | The intended state of the task. |  [optional] |
|**reachedBarrier** | **String** | The highest barrier reached by all tasks in the task&#39;s TaskGroup. |  [optional] |
|**spec** | [**TaskSpec**](TaskSpec.md) |  |  [optional] |
|**status** | [**TaskStatus**](TaskStatus.md) |  |  [optional] |
|**task** | **String** | Task name. |  [optional] |
|**taskSource** | [**TaskSourceEnum**](#TaskSourceEnum) | TaskSource represents the source of the task. |  [optional] |



## Enum: IntendedStateEnum

| Name | Value |
|---- | -----|
| INTENDED_STATE_UNSPECIFIED | &quot;INTENDED_STATE_UNSPECIFIED&quot; |
| ASSIGNED | &quot;ASSIGNED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TaskSourceEnum

| Name | Value |
|---- | -----|
| TASK_SOURCE_UNSPECIFIED | &quot;TASK_SOURCE_UNSPECIFIED&quot; |
| BATCH_INTERNAL | &quot;BATCH_INTERNAL&quot; |
| USER | &quot;USER&quot; |



