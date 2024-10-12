# DialogflowApi.GoogleCloudDialogflowV2HumanAgentAssistantEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **String** | The conversation this notification refers to. Format: &#x60;projects//conversations/&#x60;. | [optional] 
**participant** | **String** | The participant that the suggestion is compiled for. Format: &#x60;projects//conversations//participants/&#x60;. It will not be set in legacy workflow. | [optional] 
**suggestionResults** | [**[GoogleCloudDialogflowV2SuggestionResult]**](GoogleCloudDialogflowV2SuggestionResult.md) | The suggestion results payload that this notification refers to. | [optional] 


