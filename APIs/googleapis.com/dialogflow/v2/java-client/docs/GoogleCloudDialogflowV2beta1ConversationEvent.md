

# GoogleCloudDialogflowV2beta1ConversationEvent

Represents a notification sent to Pub/Sub subscribers for conversation lifecycle events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversation** | **String** | Required. The unique identifier of the conversation this notification refers to. Format: &#x60;projects//conversations/&#x60;. |  [optional] |
|**errorStatus** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**newMessagePayload** | [**GoogleCloudDialogflowV2beta1Message**](GoogleCloudDialogflowV2beta1Message.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the event that this notification refers to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CONVERSATION_STARTED | &quot;CONVERSATION_STARTED&quot; |
| CONVERSATION_FINISHED | &quot;CONVERSATION_FINISHED&quot; |
| HUMAN_INTERVENTION_NEEDED | &quot;HUMAN_INTERVENTION_NEEDED&quot; |
| NEW_MESSAGE | &quot;NEW_MESSAGE&quot; |
| UNRECOVERABLE_ERROR | &quot;UNRECOVERABLE_ERROR&quot; |



