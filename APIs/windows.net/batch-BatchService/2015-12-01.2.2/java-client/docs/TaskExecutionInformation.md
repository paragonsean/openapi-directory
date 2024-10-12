

# TaskExecutionInformation

Information about the execution of a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Gets or sets the time at which the task completed. This property is set only if the task is in the Completed state. |  [optional] |
|**exitCode** | **Integer** | Gets or sets the exit code of the task. This property is set only if the task is in completed state. |  [optional] |
|**lastRequeueTime** | **OffsetDateTime** | Gets or sets the most recent time at which the task has been requeued by the Batch service as the result of a user request. |  [optional] |
|**lastRetryTime** | **OffsetDateTime** | Gets or sets the most recent time at which a retry of the task started running. |  [optional] |
|**requeueCount** | **Integer** | Gets or sets the number of times the task has been requeued by the Batch service as the result of a user request. |  |
|**retryCount** | **Integer** | Gets or sets the number of times the task has been retried by the Batch service. |  |
|**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the time at which the task started running. If the task has been restarted or retried, this is the most recent time at which the task started running. |  [optional] |



