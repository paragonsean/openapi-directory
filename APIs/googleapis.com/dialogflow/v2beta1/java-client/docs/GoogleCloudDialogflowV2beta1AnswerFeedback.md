

# GoogleCloudDialogflowV2beta1AnswerFeedback

Represents feedback the customer has about the quality & correctness of a certain answer in a conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentAssistantDetailFeedback** | [**GoogleCloudDialogflowV2beta1AgentAssistantFeedback**](GoogleCloudDialogflowV2beta1AgentAssistantFeedback.md) |  |  [optional] |
|**clickTime** | **String** | Time when the answer/item was clicked. |  [optional] |
|**clicked** | **Boolean** | Indicates whether the answer/item was clicked by the human agent or not. Default to false. For knowledge search, the answer record is considered to be clicked if the answer was copied or any URI was clicked. |  [optional] |
|**correctnessLevel** | [**CorrectnessLevelEnum**](#CorrectnessLevelEnum) | The correctness level of the specific answer. |  [optional] |
|**displayTime** | **String** | Time when the answer/item was displayed. |  [optional] |
|**displayed** | **Boolean** | Indicates whether the answer/item was displayed to the human agent in the agent desktop UI. Default to false. |  [optional] |



## Enum: CorrectnessLevelEnum

| Name | Value |
|---- | -----|
| CORRECTNESS_LEVEL_UNSPECIFIED | &quot;CORRECTNESS_LEVEL_UNSPECIFIED&quot; |
| NOT_CORRECT | &quot;NOT_CORRECT&quot; |
| PARTIALLY_CORRECT | &quot;PARTIALLY_CORRECT&quot; |
| FULLY_CORRECT | &quot;FULLY_CORRECT&quot; |



