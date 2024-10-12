# DialogflowApi.GoogleCloudDialogflowV2beta1AnswerFeedback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentAssistantDetailFeedback** | [**GoogleCloudDialogflowV2beta1AgentAssistantFeedback**](GoogleCloudDialogflowV2beta1AgentAssistantFeedback.md) |  | [optional] 
**clickTime** | **String** | Time when the answer/item was clicked. | [optional] 
**clicked** | **Boolean** | Indicates whether the answer/item was clicked by the human agent or not. Default to false. For knowledge search, the answer record is considered to be clicked if the answer was copied or any URI was clicked. | [optional] 
**correctnessLevel** | **String** | The correctness level of the specific answer. | [optional] 
**displayTime** | **String** | Time when the answer/item was displayed. | [optional] 
**displayed** | **Boolean** | Indicates whether the answer/item was displayed to the human agent in the agent desktop UI. Default to false. | [optional] 



## Enum: CorrectnessLevelEnum


* `CORRECTNESS_LEVEL_UNSPECIFIED` (value: `"CORRECTNESS_LEVEL_UNSPECIFIED"`)

* `NOT_CORRECT` (value: `"NOT_CORRECT"`)

* `PARTIALLY_CORRECT` (value: `"PARTIALLY_CORRECT"`)

* `FULLY_CORRECT` (value: `"FULLY_CORRECT"`)




