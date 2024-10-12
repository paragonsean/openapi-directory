

# GoogleCloudDialogflowV2SuggestFaqAnswersRequest

The request message for Participants.SuggestFaqAnswers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assistQueryParams** | [**GoogleCloudDialogflowV2AssistQueryParameters**](GoogleCloudDialogflowV2AssistQueryParameters.md) |  |  [optional] |
|**contextSize** | **Integer** | Optional. Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 20 and at most 50. |  [optional] |
|**latestMessage** | **String** | Optional. The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |



