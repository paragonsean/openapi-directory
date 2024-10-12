

# TaskInformation

Information about a task running on a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  |  [optional] |
|**jobId** | **String** | The id of the job to which the task belongs. |  [optional] |
|**subtaskId** | **Integer** | The id of the subtask if the task is a multi-instance task. |  [optional] |
|**taskId** | **String** | The id of the task. |  [optional] |
|**taskState** | [**TaskStateEnum**](#TaskStateEnum) | The current state of the task. |  |
|**taskUrl** | **String** | The URL of the task. |  [optional] |



## Enum: TaskStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PREPARING | &quot;preparing&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



