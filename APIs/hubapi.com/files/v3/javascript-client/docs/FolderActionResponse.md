# FilesFiles.FolderActionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAt** | **Date** | When the requested changes have been completed. | 
**errors** | [**[StandardError]**](StandardError.md) | Detailed errors resulting from the task. | [optional] 
**links** | **{String: String}** | Link to check the status of the task. | [optional] 
**numErrors** | **Number** | Number of errors resulting from the requested changes. | [optional] 
**requestedAt** | **Date** | Timestamp representing when the task was requested. | [optional] 
**result** | [**Folder**](Folder.md) |  | [optional] 
**startedAt** | **Date** | Timestamp representing when the task was started at. | 
**status** | **String** | Current status of the task. | 
**taskId** | **String** | ID of the task. | 



## Enum: StatusEnum


* `PENDING` (value: `"PENDING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELED` (value: `"CANCELED"`)

* `COMPLETE` (value: `"COMPLETE"`)




