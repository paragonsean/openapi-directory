# BatchService.StartTaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **Date** | This is the end time of the most recent run of the start task, if that run has completed (even if that run failed and a retry is pending). This element is not present if the start task is currently running. | [optional] 
**exitCode** | **Number** | This property is set only if the start task is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the start task (due to timeout, or user termination via the API) you may see an operating system-defined exit code. | [optional] 
**lastRetryTime** | **Date** | This element is present only if the task was retried (i.e. retryCount is nonzero). If present, this is typically the same as startTime, but may be different if the task has been restarted for reasons other than retry; for example, if the compute node was rebooted during a retry, then the startTime is updated but the lastRetryTime is not. | [optional] 
**retryCount** | **Number** | The task is retried if it exits with a nonzero exit code, up to the specified MaxTaskRetryCount. | 
**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  | [optional] 
**startTime** | **Date** | This value is reset every time the task is restarted or retried (that is, this is the most recent time at which the start task started running). | 
**state** | **String** | running - The start task is currently running. completed - The start task has exited with exit code 0, or the start task has failed and the retry limit has reached, or the start task process did not run due to scheduling errors. | 



## Enum: StateEnum


* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




