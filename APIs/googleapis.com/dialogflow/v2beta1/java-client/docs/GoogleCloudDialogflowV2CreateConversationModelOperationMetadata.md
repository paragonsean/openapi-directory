

# GoogleCloudDialogflowV2CreateConversationModelOperationMetadata

Metadata for a ConversationModels.CreateConversationModel operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationModel** | **String** | The resource name of the conversation model. Format: &#x60;projects//conversationModels/&#x60; |  [optional] |
|**createTime** | **String** | Timestamp when the request to create conversation model is submitted. The time is measured on server side. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of CreateConversationModel operation. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| TRAINING | &quot;TRAINING&quot; |



