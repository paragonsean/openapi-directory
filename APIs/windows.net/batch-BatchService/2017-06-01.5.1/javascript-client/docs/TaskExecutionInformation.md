# BatchService.TaskExecutionInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | This property is set only if the task is in the Completed state. | [optional] 
**exitCode** | **Number** | This property is set only if the task is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the task (due to timeout, or user termination via the API) you may see an operating system-defined exit code. | [optional] 
**failureInfo** | [**TaskFailureInformation**](TaskFailureInformation.md) |  | [optional] 
**lastRequeueTime** | **Date** | This property is set only if the requeueCount is nonzero. | [optional] 
**lastRetryTime** | **Date** | This element is present only if the task was retried (i.e. retryCount is nonzero). If present, this is typically the same as startTime, but may be different if the task has been restarted for reasons other than retry; for example, if the compute node was rebooted during a retry, then the startTime is updated but the lastRetryTime is not. | [optional] 
**requeueCount** | **Number** | When the user removes nodes from a pool (by resizing/shrinking the pool) or when the job is being disabled, the user can specify that running tasks on the nodes be requeued for execution. This count tracks how many times the task has been requeued for these reasons. | 
**result** | [**TaskExecutionResult**](TaskExecutionResult.md) |  | [optional] 
**retryCount** | **Number** | Task application failures (non-zero exit code) are retried, pre-processing errors (the task could not be run) and file upload errors are not retried. The Batch service will retry the task up to the limit specified by the constraints. | 
**startTime** | **Date** | &#39;Running&#39; corresponds to the running state, so if the task specifies resource files or application packages, then the start time reflects the time at which the task started downloading or deploying these. If the task has been restarted or retried, this is the most recent time at which the task started running. This property is present only for tasks that are in the running or completed state. | [optional] 


