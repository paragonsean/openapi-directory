

# GoogleCloudDialogflowV2CreateConversationModelEvaluationOperationMetadata

Metadata for a ConversationModels.CreateConversationModelEvaluation operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationModel** | **String** | The resource name of the conversation model. Format: &#x60;projects//locations//conversationModels/&#x60; |  [optional] |
|**conversationModelEvaluation** | **String** | The resource name of the conversation model. Format: &#x60;projects//locations//conversationModels//evaluations/&#x60; |  [optional] |
|**createTime** | **String** | Timestamp when the request to create conversation model was submitted. The time is measured on server side. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of CreateConversationModel operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



