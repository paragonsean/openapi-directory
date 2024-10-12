# DialogflowApi.GoogleCloudDialogflowV2beta1AutomatedAgentReply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowCancellation** | **Boolean** | Indicates whether the partial automated agent reply is interruptible when a later reply message arrives. e.g. if the agent specified some music as partial response, it can be cancelled. | [optional] 
**automatedAgentReplyType** | **String** | AutomatedAgentReply type. | [optional] 
**cxCurrentPage** | **String** | The unique identifier of the current Dialogflow CX conversation page. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. | [optional] 
**cxSessionParameters** | **{String: Object}** | The collection of current Dialogflow CX agent session parameters at the time of this response. Deprecated: Use &#x60;parameters&#x60; instead. | [optional] 
**detectIntentResponse** | [**GoogleCloudDialogflowV2beta1DetectIntentResponse**](GoogleCloudDialogflowV2beta1DetectIntentResponse.md) |  | [optional] 
**event** | **String** | Event name if an event is triggered for the query. | [optional] 
**intent** | **String** | Name of the intent if an intent is matched for the query. For a V2 query, the value format is &#x60;projects//locations/ /agent/intents/&#x60;. For a V3 query, the value format is &#x60;projects//locations/ /agents//intents/&#x60;. | [optional] 
**matchConfidence** | **Number** | The confidence of the match. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. | [optional] 
**parameters** | **{String: Object}** | The collection of current parameters at the time of this response. | [optional] 
**responseMessages** | [**[GoogleCloudDialogflowV2beta1ResponseMessage]**](GoogleCloudDialogflowV2beta1ResponseMessage.md) | Response messages from the automated agent. | [optional] 



## Enum: AutomatedAgentReplyTypeEnum


* `AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED` (value: `"AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED"`)

* `PARTIAL` (value: `"PARTIAL"`)

* `FINAL` (value: `"FINAL"`)




