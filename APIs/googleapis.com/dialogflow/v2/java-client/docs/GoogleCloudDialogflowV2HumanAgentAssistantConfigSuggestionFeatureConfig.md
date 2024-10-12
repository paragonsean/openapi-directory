

# GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig

Config for suggestion features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationModelConfig** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfig**](GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationModelConfig.md) |  |  [optional] |
|**conversationProcessConfig** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfig**](GoogleCloudDialogflowV2HumanAgentAssistantConfigConversationProcessConfig.md) |  |  [optional] |
|**disableAgentQueryLogging** | **Boolean** | Optional. Disable the logging of search queries sent by human agents. It can prevent those queries from being stored at answer records. Supported features: KNOWLEDGE_SEARCH. |  [optional] |
|**enableConversationAugmentedQuery** | **Boolean** | Optional. Enable including conversation context during query answer generation. Supported features: KNOWLEDGE_SEARCH. |  [optional] |
|**enableEventBasedSuggestion** | **Boolean** | Automatically iterates all participants and tries to compile suggestions. Supported features: ARTICLE_SUGGESTION, FAQ, DIALOGFLOW_ASSIST, KNOWLEDGE_ASSIST. |  [optional] |
|**queryConfig** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfig**](GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionQueryConfig.md) |  |  [optional] |
|**suggestionFeature** | [**GoogleCloudDialogflowV2SuggestionFeature**](GoogleCloudDialogflowV2SuggestionFeature.md) |  |  [optional] |
|**suggestionTriggerSettings** | [**GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettings**](GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionTriggerSettings.md) |  |  [optional] |



