# DialogflowApi.GoogleCloudDialogflowV2AutomatedAgentReply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowCancellation** | **Boolean** | Indicates whether the partial automated agent reply is interruptible when a later reply message arrives. e.g. if the agent specified some music as partial response, it can be cancelled. | [optional] 
**automatedAgentReplyType** | **String** | AutomatedAgentReply type. | [optional] 
**cxCurrentPage** | **String** | The unique identifier of the current Dialogflow CX conversation page. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. | [optional] 
**detectIntentResponse** | [**GoogleCloudDialogflowV2DetectIntentResponse**](GoogleCloudDialogflowV2DetectIntentResponse.md) |  | [optional] 



## Enum: AutomatedAgentReplyTypeEnum


* `AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED` (value: `"AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED"`)

* `PARTIAL` (value: `"PARTIAL"`)

* `FINAL` (value: `"FINAL"`)




