# DialogflowApi.GoogleCloudDialogflowV2beta1HumanAgentAssistantEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | **String** | The conversation this notification refers to. Format: &#x60;projects//conversations/&#x60;. | [optional] 
**participant** | **String** | The participant that the suggestion is compiled for. And This field is used to call Participants.ListSuggestions API. Format: &#x60;projects//conversations//participants/&#x60;. It will not be set in legacy workflow. HumanAgentAssistantConfig.name for more information. | [optional] 
**suggestionResults** | [**[GoogleCloudDialogflowV2beta1SuggestionResult]**](GoogleCloudDialogflowV2beta1SuggestionResult.md) | The suggestion results payload that this notification refers to. It will only be set when HumanAgentAssistantConfig.SuggestionConfig.group_suggestion_responses sets to true. | [optional] 


