

# JobReleaseTaskExecutionInformation

Contains information about the execution of a Job Release task on a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | The time at which the Job Release task completed. This property is set only if the task is in the Completed state. |  [optional] |
|**exitCode** | **Integer** | The exit code of the Job Release task. This property is set only if the task is in the Completed state. |  [optional] |
|**schedulingError** | [**TaskSchedulingError**](TaskSchedulingError.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The time at which the task started running. Note that every time the task is restarted, this value is updated. |  |
|**state** | [**StateEnum**](#StateEnum) | The current state of the Job Release task. |  |
|**taskRootDirectory** | **String** | The root directory of the Job Release task on the compute node. You can use this path to retrieve files created by the task, such as log files. |  [optional] |
|**taskRootDirectoryUrl** | **String** | The URL to the root directory of the Job Release task on the compute node. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



