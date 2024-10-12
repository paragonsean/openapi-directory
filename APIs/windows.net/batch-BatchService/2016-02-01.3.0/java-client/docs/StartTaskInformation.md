

# StartTaskInformation

Information about a start task running on a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The time at which the start task stopped running. |  [optional] |
|**exitCode** | **Integer** | The exit code of the start task. |  [optional] |
|**lastRetryTime** | **OffsetDateTime** | The most recent time at which a retry of the task started running. |  [optional] |
|**retryCount** | **Integer** | The number of times the task has been retried by the Batch service. |  |
|**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The time at which the start task started running. |  |
|**state** | [**StateEnum**](#StateEnum) | The state of the start task on the compute node. |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



