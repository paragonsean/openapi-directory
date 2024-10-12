# BatchService.StartTaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | Gets or sets the time at which the start task stopped running. | [optional] 
**exitCode** | **Number** | Gets or sets the exit code of the start task. | [optional] 
**lastRetryTime** | **Date** | Gets or sets the most recent time at which a retry of the task started running. | [optional] 
**retryCount** | **Number** | Gets or sets the number of times the task has been retried by the Batch service. | 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | Gets or sets the time at which the start task started running. | 
**state** | **String** | Gets or sets the state of the start task on the compute node. | 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




