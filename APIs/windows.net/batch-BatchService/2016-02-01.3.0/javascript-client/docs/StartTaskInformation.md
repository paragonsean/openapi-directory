# BatchService.StartTaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The time at which the start task stopped running. | [optional] 
**exitCode** | **Number** | The exit code of the start task. | [optional] 
**lastRetryTime** | **Date** | The most recent time at which a retry of the task started running. | [optional] 
**retryCount** | **Number** | The number of times the task has been retried by the Batch service. | 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | The time at which the start task started running. | 
**state** | **String** | The state of the start task on the compute node. | 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




