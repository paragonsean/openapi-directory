# BatchService.TaskAddResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eTag** | **String** | You can use this to detect whether the task has changed between requests. In particular, you can be pass the ETag with an Update Task request to specify that your changes should take effect only if nobody else has modified the job in the meantime. | [optional] 
**error** | [**BatchError**](BatchError.md) |  | [optional] 
**lastModified** | **Date** |  | [optional] 
**location** | **String** |  | [optional] 
**status** | **String** | Values are:   success - Task was added successfully.  clienterror - Task failed to add due to a client error and should not be retried without modifying the request as appropriate.  servererror - Task failed to add due to a server error and can be retried without modification. | 
**taskId** | **String** |  | 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `clientError` (value: `"clientError"`)

* `serverError` (value: `"serverError"`)




