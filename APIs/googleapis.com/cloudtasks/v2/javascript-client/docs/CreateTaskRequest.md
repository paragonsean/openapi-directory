# CloudTasksApi.CreateTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responseView** | **String** | The response_view specifies which subset of the Task will be returned. By default response_view is BASIC; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains. Authorization for FULL requires &#x60;cloudtasks.tasks.fullView&#x60; [Google IAM](https://cloud.google.com/iam/) permission on the Task resource. | [optional] 
**task** | [**Task**](Task.md) |  | [optional] 



## Enum: ResponseViewEnum


* `VIEW_UNSPECIFIED` (value: `"VIEW_UNSPECIFIED"`)

* `BASIC` (value: `"BASIC"`)

* `FULL` (value: `"FULL"`)




