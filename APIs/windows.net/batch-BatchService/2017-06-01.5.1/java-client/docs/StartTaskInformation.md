

# StartTaskInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | This is the end time of the most recent run of the start task, if that run has completed (even if that run failed and a retry is pending). This element is not present if the start task is currently running. |  [optional] |
|**exitCode** | **Integer** | This property is set only if the start task is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the start task (due to timeout, or user termination via the API) you may see an operating system-defined exit code. |  [optional] |
|**failureInfo** | [**TaskFailureInformation**](TaskFailureInformation.md) |  |  [optional] |
|**lastRetryTime** | **OffsetDateTime** | This element is present only if the task was retried (i.e. retryCount is nonzero). If present, this is typically the same as startTime, but may be different if the task has been restarted for reasons other than retry; for example, if the compute node was rebooted during a retry, then the startTime is updated but the lastRetryTime is not. |  [optional] |
|**result** | **TaskExecutionResult** |  |  [optional] |
|**retryCount** | **Integer** | Task application failures (non-zero exit code) are retried, pre-processing errors (the task could not be run) and file upload errors are not retried. The Batch service will retry the task up to the limit specified by the constraints. |  |
|**startTime** | **OffsetDateTime** | This value is reset every time the task is restarted or retried (that is, this is the most recent time at which the start task started running). |  |
|**state** | [**StateEnum**](#StateEnum) | Values are:   running - The start task is currently running.  completed - The start task has exited with exit code 0, or the start task has failed and the retry limit has reached, or the start task process did not run due to task preparation errors (such as resource file download failures). |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



