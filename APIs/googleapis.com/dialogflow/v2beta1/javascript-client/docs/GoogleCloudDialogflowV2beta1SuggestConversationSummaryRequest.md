# DialogflowApi.GoogleCloudDialogflowV2beta1SuggestConversationSummaryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assistQueryParams** | [**GoogleCloudDialogflowV2beta1AssistQueryParameters**](GoogleCloudDialogflowV2beta1AssistQueryParameters.md) |  | [optional] 
**contextSize** | **Number** | Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 500 and at most 1000. | [optional] 
**latestMessage** | **String** | The name of the latest conversation message used as context for compiling suggestion. If empty, the latest message of the conversation will be used. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 


