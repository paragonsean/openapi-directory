

# GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionFeatureConfig

Config for suggestion features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversationModelConfig** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigConversationModelConfig**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigConversationModelConfig.md) |  |  [optional] |
|**conversationProcessConfig** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigConversationProcessConfig**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigConversationProcessConfig.md) |  |  [optional] |
|**disableAgentQueryLogging** | **Boolean** | Optional. Disable the logging of search queries sent by human agents. It can prevent those queries from being stored at answer records. Supported features: KNOWLEDGE_SEARCH. |  [optional] |
|**enableConversationAugmentedQuery** | **Boolean** | Optional. Enable including conversation context during query answer generation. Supported features: KNOWLEDGE_SEARCH. |  [optional] |
|**enableEventBasedSuggestion** | **Boolean** | Automatically iterates all participants and tries to compile suggestions. Supported features: ARTICLE_SUGGESTION, FAQ, DIALOGFLOW_ASSIST, ENTITY_EXTRACTION, KNOWLEDGE_ASSIST. |  [optional] |
|**queryConfig** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfig**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfig.md) |  |  [optional] |
|**suggestionFeature** | [**GoogleCloudDialogflowV2beta1SuggestionFeature**](GoogleCloudDialogflowV2beta1SuggestionFeature.md) |  |  [optional] |
|**suggestionTriggerSettings** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionTriggerSettings**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionTriggerSettings.md) |  |  [optional] |



