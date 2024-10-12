# DialogflowApi.GoogleCloudDialogflowV2SuggestSmartRepliesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextSize** | **Number** | Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 20 and at most 50. | [optional] 
**currentTextInput** | [**GoogleCloudDialogflowV2TextInput**](GoogleCloudDialogflowV2TextInput.md) |  | [optional] 
**latestMessage** | **String** | The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation. Format: &#x60;projects//locations//conversations//messages/&#x60;. | [optional] 


