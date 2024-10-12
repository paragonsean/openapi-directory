# BatchService.TaskExecutionInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | The time at which the task completed. This property is set only if the task is in the Completed state. | [optional] 
**exitCode** | **Number** | The exit code of the task. This property is set only if the task is in completed state. | [optional] 
**lastRequeueTime** | **Date** | The most recent time at which the task has been requeued by the Batch service as the result of a user request. | [optional] 
**lastRetryTime** | **Date** | The most recent time at which a retry of the task started running. | [optional] 
**requeueCount** | **Number** | The number of times the task has been requeued by the Batch service as the result of a user request. | 
**retryCount** | **Number** | The number of times the task has been retried by the Batch service. | 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | The time at which the task started running. If the task has been restarted or retried, this is the most recent time at which the task started running. | [optional] 


