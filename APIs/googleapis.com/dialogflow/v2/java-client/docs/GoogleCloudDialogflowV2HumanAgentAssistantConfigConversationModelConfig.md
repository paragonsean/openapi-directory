

# GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfig

Custom conversation models used in agent assist feature. Supported feature: ARTICLE_SUGGESTION, SMART_COMPOSE, SMART_REPLY, CONVERSATION_SUMMARIZATION.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baselineModelVersion** | **String** | Version of current baseline model. It will be ignored if model is set. Valid versions are: Article Suggestion baseline model: - 0.9 - 1.0 (default) Summarization baseline model: - 1.0 |  [optional] |
|**model** | **String** | Conversation model resource name. Format: &#x60;projects//conversationModels/&#x60;. |  [optional] |



