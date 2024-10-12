# BatchService.StartTaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerInfo** | [**TaskContainerExecutionInformation**](TaskContainerExecutionInformation.md) |  | [optional] 
**endTime** | **Date** | This is the end time of the most recent run of the start Task, if that run has completed (even if that run failed and a retry is pending). This element is not present if the start Task is currently running. | [optional] 
**exitCode** | **Number** | This property is set only if the start Task is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the start Task (due to timeout, or user termination via the API) you may see an operating system-defined exit code. | [optional] 
**failureInfo** | [**TaskFailureInformation**](TaskFailureInformation.md) |  | [optional] 
**lastRetryTime** | **Date** | This element is present only if the Task was retried (i.e. retryCount is nonzero). If present, this is typically the same as startTime, but may be different if the Task has been restarted for reasons other than retry; for example, if the Compute Node was rebooted during a retry, then the startTime is updated but the lastRetryTime is not. | [optional] 
**result** | [**TaskExecutionResult**](TaskExecutionResult.md) |  | [optional] 
**retryCount** | **Number** | Task application failures (non-zero exit code) are retried, pre-processing errors (the Task could not be run) and file upload errors are not retried. The Batch service will retry the Task up to the limit specified by the constraints. | 
**startTime** | **Date** | This value is reset every time the Task is restarted or retried (that is, this is the most recent time at which the start Task started running). | 
**state** | **String** |  | 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




