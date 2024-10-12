

# GoogleCloudDialogflowV2Conversation

Represents a conversation. A conversation is an interaction between an agent, including live agents and Dialogflow agents, and a support customer. Conversations can include phone calls and text-based chat sessions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationProfile** | **String** | Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: &#x60;projects//locations//conversationProfiles/&#x60;. |  [optional] |
|**conversationStage** | [**ConversationStageEnum**](#ConversationStageEnum) | The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE. |  [optional] |
|**endTime** | **String** | Output only. The time the conversation was finished. |  [optional] [readonly] |
|**lifecycleState** | [**LifecycleStateEnum**](#LifecycleStateEnum) | Output only. The current state of the Conversation. |  [optional] [readonly] |
|**name** | **String** | Output only. The unique identifier of this conversation. Format: &#x60;projects//locations//conversations/&#x60;. |  [optional] [readonly] |
|**phoneNumber** | [**GoogleCloudDialogflowV2ConversationPhoneNumber**](GoogleCloudDialogflowV2ConversationPhoneNumber.md) |  |  [optional] |
|**startTime** | **String** | Output only. The time the conversation was started. |  [optional] [readonly] |



## Enum: ConversationStageEnum

| Name | Value |
|---- | -----|
| CONVERSATION_STAGE_UNSPECIFIED | &quot;CONVERSATION_STAGE_UNSPECIFIED&quot; |
| VIRTUAL_AGENT_STAGE | &quot;VIRTUAL_AGENT_STAGE&quot; |
| HUMAN_ASSIST_STAGE | &quot;HUMAN_ASSIST_STAGE&quot; |



## Enum: LifecycleStateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



