# BatchService.TaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  | [optional] 
**jobId** | **String** | The id of the job to which the task belongs. | [optional] 
**subtaskId** | **Number** | The id of the subtask if the task is a multi-instance task. | [optional] 
**taskId** | **String** | The id of the task. | [optional] 
**taskState** | **String** | The current state of the task. | 
**taskUrl** | **String** | The URL of the task. | [optional] 



## Enum: TaskStateEnum


* `active` (value: `"active"`)

* `preparing` (value: `"preparing"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




