

# GoogleCloudDialogflowV2HumanAgentAssistantEvent

Represents a notification sent to Cloud Pub/Sub subscribers for human agent assistant events in a specific conversation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversation** | **String** | The conversation this notification refers to. Format: &#x60;projects//conversations/&#x60;. |  [optional] |
|**participant** | **String** | The participant that the suggestion is compiled for. Format: &#x60;projects//conversations//participants/&#x60;. It will not be set in legacy workflow. |  [optional] |
|**suggestionResults** | [**List&lt;GoogleCloudDialogflowV2SuggestionResult&gt;**](GoogleCloudDialogflowV2SuggestionResult.md) | The suggestion results payload that this notification refers to. |  [optional] |



