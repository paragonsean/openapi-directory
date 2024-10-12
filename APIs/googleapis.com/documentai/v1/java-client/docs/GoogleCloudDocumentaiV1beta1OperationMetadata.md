

# GoogleCloudDocumentaiV1beta1OperationMetadata

Contains metadata for the BatchProcessDocuments operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The creation time of the operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the current batch processing. |  [optional] |
|**stateMessage** | **String** | A message providing more details about the current state of processing. |  [optional] |
|**updateTime** | **String** | The last update time of the operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| WAITING | &quot;WAITING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |



