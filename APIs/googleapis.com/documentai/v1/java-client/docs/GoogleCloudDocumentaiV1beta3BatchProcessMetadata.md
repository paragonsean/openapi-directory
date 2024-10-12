

# GoogleCloudDocumentaiV1beta3BatchProcessMetadata

The long-running operation metadata for BatchProcessDocuments.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The creation time of the operation. |  [optional] |
|**individualProcessStatuses** | [**List&lt;GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus&gt;**](GoogleCloudDocumentaiV1beta3BatchProcessMetadataIndividualProcessStatus.md) | The list of response details of each document. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The state of the current batch processing. |  [optional] |
|**stateMessage** | **String** | A message providing more details about the current state of processing. For example, the error message if the operation is failed. |  [optional] |
|**updateTime** | **String** | The last update time of the operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| WAITING | &quot;WAITING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |



