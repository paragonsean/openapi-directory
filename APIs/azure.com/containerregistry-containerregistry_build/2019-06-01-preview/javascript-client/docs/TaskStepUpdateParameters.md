# ContainerRegistryManagementClient.TaskStepUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextAccessToken** | **String** | The token (git PAT or SAS token of storage account blob) associated with the context for a step. | [optional] 
**contextPath** | **String** | The URL(absolute or relative) of the source context for the task step. | [optional] 
**type** | **String** | The type of the step. | 



## Enum: TypeEnum


* `Docker` (value: `"Docker"`)

* `FileTask` (value: `"FileTask"`)

* `EncodedTask` (value: `"EncodedTask"`)




