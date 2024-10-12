# BatchService.TaskInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionInfo** | [**TaskExecutionInformation**](TaskExecutionInformation.md) |  | [optional] 
**jobId** | **String** | Gets or sets the id of the job to which the task belongs. | [optional] 
**subtaskId** | **Number** | Gets or sets the id of the subtask if the task is a multi-instance task. | [optional] 
**taskId** | **String** | Gets or sets the id of the task. | [optional] 
**taskState** | **String** | Gets or sets the current state of the task. | 
**taskUrl** | **String** | Gets or sets the URL of the task. | [optional] 



## Enum: TaskStateEnum


* `active` (value: `"active"`)

* `preparing` (value: `"preparing"`)

* `running` (value: `"running"`)

* `completed` (value: `"completed"`)




