

# TaskInformation

Information about a task running on a compute node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  |  [optional] |
|**jobId** | **String** | Gets or sets the id of the job to which the task belongs. |  [optional] |
|**subtaskId** | **Integer** | Gets or sets the id of the subtask if the task is a multi-instance task. |  [optional] |
|**taskId** | **String** | Gets or sets the id of the task. |  [optional] |
|**taskState** | [**TaskStateEnum**](#TaskStateEnum) | Gets or sets the current state of the task. |  |
|**taskUrl** | **String** | Gets or sets the URL of the task. |  [optional] |



## Enum: TaskStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PREPARING | &quot;preparing&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |



