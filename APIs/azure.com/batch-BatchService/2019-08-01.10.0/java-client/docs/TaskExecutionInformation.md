

# TaskExecutionInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerInfo** | [**TaskContainerExecutionInformation**](TaskContainerExecutionInformation.md) |  |  [optional] |
|**endTime** | **OffsetDateTime** | This property is set only if the Task is in the Completed state. |  [optional] |
|**exitCode** | **Integer** | This property is set only if the Task is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the Task (due to timeout, or user termination via the API) you may see an operating system-defined exit code. |  [optional] |
|**failureInfo** | [**TaskFailureInformation**](TaskFailureInformation.md) |  |  [optional] |
|**lastRequeueTime** | **OffsetDateTime** | This property is set only if the requeueCount is nonzero. |  [optional] |
|**lastRetryTime** | **OffsetDateTime** | This element is present only if the Task was retried (i.e. retryCount is nonzero). If present, this is typically the same as startTime, but may be different if the Task has been restarted for reasons other than retry; for example, if the Compute Node was rebooted during a retry, then the startTime is updated but the lastRetryTime is not. |  [optional] |
|**requeueCount** | **Integer** | When the user removes Compute Nodes from a Pool (by resizing/shrinking the pool) or when the Job is being disabled, the user can specify that running Tasks on the Compute Nodes be requeued for execution. This count tracks how many times the Task has been requeued for these reasons. |  |
|**result** | **TaskExecutionResult** |  |  [optional] |
|**retryCount** | **Integer** | Task application failures (non-zero exit code) are retried, pre-processing errors (the Task could not be run) and file upload errors are not retried. The Batch service will retry the Task up to the limit specified by the constraints. |  |
|**startTime** | **OffsetDateTime** | &#39;Running&#39; corresponds to the running state, so if the Task specifies resource files or Packages, then the start time reflects the time at which the Task started downloading or deploying these. If the Task has been restarted or retried, this is the most recent time at which the Task started running. This property is present only for Tasks that are in the running or completed state. |  [optional] |



