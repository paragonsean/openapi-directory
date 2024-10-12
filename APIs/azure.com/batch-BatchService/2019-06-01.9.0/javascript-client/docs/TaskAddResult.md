# BatchService.TaskAddResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eTag** | **String** | You can use this to detect whether the Task has changed between requests. In particular, you can be pass the ETag with an Update Task request to specify that your changes should take effect only if nobody else has modified the Job in the meantime. | [optional] 
**error** | [**BatchError**](BatchError.md) |  | [optional] 
**lastModified** | **Date** |  | [optional] 
**location** | **String** |  | [optional] 
**status** | **String** |  | 
**taskId** | **String** |  | 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `clienterror` (value: `"clienterror"`)

* `servererror` (value: `"servererror"`)




