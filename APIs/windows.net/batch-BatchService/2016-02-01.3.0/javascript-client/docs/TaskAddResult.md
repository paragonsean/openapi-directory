# BatchService.TaskAddResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eTag** | **String** | The ETag of the task, if the task was successfully added. | [optional] 
**error** | [**BatchError**](BatchError.md) |  | [optional] 
**lastModified** | **Date** | The last modified time of the task. | [optional] 
**location** | **String** | The URL of the task, if the task was successfully added. | [optional] 
**status** | **String** | The status of the add task request. | 
**taskId** | **String** | The id of the task for which this is the result. | 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `clienterror` (value: `"clienterror"`)

* `servererror` (value: `"servererror"`)

* `unmapped` (value: `"unmapped"`)




