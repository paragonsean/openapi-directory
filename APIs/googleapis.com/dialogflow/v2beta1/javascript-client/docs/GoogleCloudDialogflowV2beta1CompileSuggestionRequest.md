# DialogflowApi.GoogleCloudDialogflowV2beta1CompileSuggestionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextSize** | **Number** | Optional. Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. If zero or less than zero, 20 is used. | [optional] 
**latestMessage** | **String** | Optional. The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 


