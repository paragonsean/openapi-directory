

# GoogleCloudDialogflowV2SuggestConversationSummaryRequest

The request message for Conversations.SuggestConversationSummary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assistQueryParams** | [**GoogleCloudDialogflowV2AssistQueryParameters**](GoogleCloudDialogflowV2AssistQueryParameters.md) |  |  [optional] |
|**contextSize** | **Integer** | Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 500 and at most 1000. |  [optional] |
|**latestMessage** | **String** | The name of the latest conversation message used as context for compiling suggestion. If empty, the latest message of the conversation will be used. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |



