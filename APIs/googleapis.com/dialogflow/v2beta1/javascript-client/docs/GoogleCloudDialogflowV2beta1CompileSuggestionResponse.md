# DialogflowApi.GoogleCloudDialogflowV2beta1CompileSuggestionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextSize** | **Number** | Number of messages prior to and including latest_message to compile the suggestion. It may be smaller than the CompileSuggestionRequest.context_size field in the request if there aren&#39;t that many messages in the conversation. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used to compile suggestion for. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 
**suggestion** | [**GoogleCloudDialogflowV2beta1Suggestion**](GoogleCloudDialogflowV2beta1Suggestion.md) |  | [optional] 


