

# GoogleCloudDocumentaiV1beta3ReviewDocumentOperationMetadata

The long-running operation metadata for the ReviewDocument method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonMetadata** | [**GoogleCloudDocumentaiV1beta3CommonOperationMetadata**](GoogleCloudDocumentaiV1beta3CommonOperationMetadata.md) |  |  [optional] |
|**createTime** | **String** | The creation time of the operation. |  [optional] |
|**questionId** | **String** | The Crowd Compute question ID. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Used only when Operation.done is false. |  [optional] |
|**stateMessage** | **String** | A message providing more details about the current state of processing. For example, the error message if the operation is failed. |  [optional] |
|**updateTime** | **String** | The last update time of the operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



