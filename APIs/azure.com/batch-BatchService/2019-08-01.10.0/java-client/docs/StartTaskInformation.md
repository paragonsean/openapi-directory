

# StartTaskInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerInfo** | [**TaskContainerExecutionInformation**](TaskContainerExecutionInformation.md) |  |  [optional] |
|**endTime** | **OffsetDateTime** | This is the end time of the most recent run of the StartTask, if that run has completed (even if that run failed and a retry is pending). This element is not present if the StartTask is currently running. |  [optional] |
|**exitCode** | **Integer** | This property is set only if the StartTask is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the StartTask (due to timeout, or user termination via the API) you may see an operating system-defined exit code. |  [optional] |
|**failureInfo** | [**TaskFailureInformation**](TaskFailureInformation.md) |  |  [optional] |
|**lastRetryTime** | **OffsetDateTime** | This element is present only if the Task was retried (i.e. retryCount is nonzero). If present, this is typically the same as startTime, but may be different if the Task has been restarted for reasons other than retry; for example, if the Compute Node was rebooted during a retry, then the startTime is updated but the lastRetryTime is not. |  [optional] |
|**result** | **TaskExecutionResult** |  |  [optional] |
|**retryCount** | **Integer** | Task application failures (non-zero exit code) are retried, pre-processing errors (the Task could not be run) and file upload errors are not retried. The Batch service will retry the Task up to the limit specified by the constraints. |  |
|**startTime** | **OffsetDateTime** | This value is reset every time the Task is restarted or retried (that is, this is the most recent time at which the StartTask started running). |  |
|**state** | [**StateEnum**](#StateEnum) |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



