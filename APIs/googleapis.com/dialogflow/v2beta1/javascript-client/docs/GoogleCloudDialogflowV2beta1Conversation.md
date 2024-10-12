# DialogflowApi.GoogleCloudDialogflowV2beta1Conversation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversationProfile** | **String** | Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: &#x60;projects//locations//conversationProfiles/&#x60;. | [optional] 
**conversationStage** | **String** | The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation. If the conversation is created with the conversation profile that has Dialogflow config set, defaults to ConversationStage.VIRTUAL_AGENT_STAGE; Otherwise, defaults to ConversationStage.HUMAN_ASSIST_STAGE. If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversation_stage to ConversationStage.HUMAN_ASSIST_STAGE, it skips ConversationStage.VIRTUAL_AGENT_STAGE stage and directly goes to ConversationStage.HUMAN_ASSIST_STAGE. | [optional] 
**endTime** | **String** | Output only. The time the conversation was finished. | [optional] [readonly] 
**lifecycleState** | **String** | Output only. The current state of the Conversation. | [optional] [readonly] 
**name** | **String** | Output only. The unique identifier of this conversation. Format: &#x60;projects//locations//conversations/&#x60;. | [optional] [readonly] 
**phoneNumber** | [**GoogleCloudDialogflowV2beta1ConversationPhoneNumber**](GoogleCloudDialogflowV2beta1ConversationPhoneNumber.md) |  | [optional] 
**startTime** | **String** | Output only. The time the conversation was started. | [optional] [readonly] 



## Enum: ConversationStageEnum


* `CONVERSATION_STAGE_UNSPECIFIED` (value: `"CONVERSATION_STAGE_UNSPECIFIED"`)

* `VIRTUAL_AGENT_STAGE` (value: `"VIRTUAL_AGENT_STAGE"`)

* `HUMAN_ASSIST_STAGE` (value: `"HUMAN_ASSIST_STAGE"`)





## Enum: LifecycleStateEnum


* `LIFECYCLE_STATE_UNSPECIFIED` (value: `"LIFECYCLE_STATE_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `COMPLETED` (value: `"COMPLETED"`)




