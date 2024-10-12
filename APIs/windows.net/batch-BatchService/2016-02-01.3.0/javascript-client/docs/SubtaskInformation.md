# BatchService.SubtaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The time at which the subtask completed. This property is set only if the subtask is in the Completed state. | [optional] 
**exitCode** | **Number** | The exit code of the subtask. This property is set only if the subtask is in the Completed state. | [optional] 
**id** | **Number** | The id of the subtask. | [optional] 
**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  | [optional] 
**previousState** | **String** | The previous state of the subtask. This property is not set if the subtask is in its initial Active state. | [optional] 
**previousStateTransitionTime** | **Date** | The time at which the subtask entered its previous state. This property is not set if the subtask is in its initial Active state. | [optional] 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | The time at which the subtask started running. If the subtask has been restarted or retried, this is the most recent time at which the subtask started running. | [optional] 
**state** | **String** | The current state of the subtask. | [optional] 
**stateTransitionTime** | **Date** | The time at which the subtask entered its current state. | [optional] 



## Enum: PreviousStateEnum


* `active` (value: `"active"`)

* `preparing` (value: `"preparing"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `preparing` (value: `"preparing"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




