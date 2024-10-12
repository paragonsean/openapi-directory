

# GoogleCloudDocumentaiUiv1beta3CommonOperationMetadata

The common metadata for long running operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The creation time of the operation. |  [optional] |
|**resource** | **String** | A related resource to this operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the operation. |  [optional] |
|**stateMessage** | **String** | A message providing more details about the current state of processing. |  [optional] |
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



