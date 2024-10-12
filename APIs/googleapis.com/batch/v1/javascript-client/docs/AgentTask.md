# BatchApi.AgentTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentTaskSpec** | [**AgentTaskSpec**](AgentTaskSpec.md) |  | [optional] 
**intendedState** | **String** | The intended state of the task. | [optional] 
**reachedBarrier** | **String** | The highest barrier reached by all tasks in the task&#39;s TaskGroup. | [optional] 
**spec** | [**TaskSpec**](TaskSpec.md) |  | [optional] 
**status** | [**TaskStatus**](TaskStatus.md) |  | [optional] 
**task** | **String** | Task name. | [optional] 
**taskSource** | **String** | TaskSource represents the source of the task. | [optional] 



## Enum: IntendedStateEnum


* `INTENDED_STATE_UNSPECIFIED` (value: `"INTENDED_STATE_UNSPECIFIED"`)

* `ASSIGNED` (value: `"ASSIGNED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: TaskSourceEnum


* `TASK_SOURCE_UNSPECIFIED` (value: `"TASK_SOURCE_UNSPECIFIED"`)

* `BATCH_INTERNAL` (value: `"BATCH_INTERNAL"`)

* `USER` (value: `"USER"`)




