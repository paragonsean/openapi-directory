# FilesFiles.FileActionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAt** | **Date** | Time of completion of task. | 
**errors** | [**[StandardError]**](StandardError.md) | Descriptive error messages. | [optional] 
**links** | **{String: String}** | Link to check the status of the requested task. | [optional] 
**numErrors** | **Number** | Number of errors resulting from the task. | [optional] 
**requestedAt** | **Date** | Timestamp of when the task was requested. | [optional] 
**result** | **File** |  | [optional] 
**startedAt** | **Date** | Timestamp of when the task was started. | 
**status** | **String** | Current status of the task. | 
**taskId** | **String** | ID of the requested task. | 



## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELED` (value: `"CANCELED"`)

* `COMPLETE` (value: `"COMPLETE"`)




