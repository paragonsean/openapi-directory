# DialogflowApi.GoogleCloudDialogflowV2ConversationEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **String** | The unique identifier of the conversation this notification refers to. Format: &#x60;projects//conversations/&#x60;. | [optional] 
**errorStatus** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**newMessagePayload** | [**GoogleCloudDialogflowV2Message**](GoogleCloudDialogflowV2Message.md) |  | [optional] 
**type** | **String** | The type of the event that this notification refers to. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `CONVERSATION_STARTED` (value: `"CONVERSATION_STARTED"`)

* `CONVERSATION_FINISHED` (value: `"CONVERSATION_FINISHED"`)

* `HUMAN_INTERVENTION_NEEDED` (value: `"HUMAN_INTERVENTION_NEEDED"`)

* `NEW_MESSAGE` (value: `"NEW_MESSAGE"`)

* `UNRECOVERABLE_ERROR` (value: `"UNRECOVERABLE_ERROR"`)




