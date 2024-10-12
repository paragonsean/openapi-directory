

# GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponse

The response message for Conversations.SuggestConversationSummary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contextSize** | **Integer** | Number of messages prior to and including last_conversation_message used to compile the suggestion. It may be smaller than the SuggestSummaryRequest.context_size field in the request if there weren&#39;t that many messages in the conversation. |  [optional] |
|**latestMessage** | **String** | The name of the latest conversation message used as context for compiling suggestion. Format: &#x60;projects//locations//conversations//messages/&#x60;. |  [optional] |
|**summary** | [**GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponseSummary**](GoogleCloudDialogflowV2beta1SuggestConversationSummaryResponseSummary.md) |  |  [optional] |



