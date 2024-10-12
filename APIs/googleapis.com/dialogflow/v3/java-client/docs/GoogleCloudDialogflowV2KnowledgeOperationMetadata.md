

# GoogleCloudDialogflowV2KnowledgeOperationMetadata

Metadata in google::longrunning::Operation for Knowledge operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportOperationMetadata** | [**GoogleCloudDialogflowV2ExportOperationMetadata**](GoogleCloudDialogflowV2ExportOperationMetadata.md) |  |  [optional] |
|**knowledgeBase** | **String** | The name of the knowledge base interacted with during the operation. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of this operation. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |



