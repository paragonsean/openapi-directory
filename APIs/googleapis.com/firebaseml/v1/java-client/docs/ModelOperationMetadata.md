

# ModelOperationMetadata

This is returned in the longrunning operations for create/update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicOperationStatus** | [**BasicOperationStatusEnum**](#BasicOperationStatusEnum) |  |  [optional] |
|**name** | **String** | The name of the model we are creating/updating The name must have the form &#x60;projects/{project_id}/models/{model_id}&#x60; |  [optional] |



## Enum: BasicOperationStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BASIC_OPERATION_STATUS_UNSPECIFIED&quot; |
| UPLOADING | &quot;BASIC_OPERATION_STATUS_UPLOADING&quot; |
| VERIFYING | &quot;BASIC_OPERATION_STATUS_VERIFYING&quot; |



