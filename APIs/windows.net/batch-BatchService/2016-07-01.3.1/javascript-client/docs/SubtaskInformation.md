# BatchService.SubtaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | This property is set only if the subtask is in the Completed state. | [optional] 
**exitCode** | **Number** | This property is set only if the subtask is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the subtask (due to timeout, or user termination via the API) you may see an operating system-defined exit code. | [optional] 
**id** | **Number** |  | [optional] 
**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  | [optional] 
**previousState** | **String** | This property is not set if the subtask is in its initial running state. | [optional] 
**previousStateTransitionTime** | **Date** | This property is not set if the subtask is in its initial running state. | [optional] 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** |  | [optional] 
**state** | **String** |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 



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




