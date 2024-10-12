

# GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfig

Config for suggestion query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceThreshold** | **Float** | Confidence threshold of query result. Agent Assist gives each suggestion a score in the range [0.0, 1.0], based on the relevance between the suggestion and the current conversation context. A score of 0.0 has no relevance, while a score of 1.0 has high relevance. Only suggestions with a score greater than or equal to the value of this field are included in the results. For a baseline model (the default), the recommended value is in the range [0.05, 0.1]. For a custom model, there is no recommended value. Tune this value by starting from a very low value and slowly increasing until you have desired results. If this field is not set, it is default to 0.0, which means that all suggestions are returned. Supported features: ARTICLE_SUGGESTION, FAQ, SMART_REPLY, SMART_COMPOSE, KNOWLEDGE_SEARCH, KNOWLEDGE_ASSIST, ENTITY_EXTRACTION. |  [optional] |
|**contextFilterSettings** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigContextFilterSettings**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigContextFilterSettings.md) |  |  [optional] |
|**dialogflowQuerySource** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySource**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigDialogflowQuerySource.md) |  |  [optional] |
|**documentQuerySource** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigDocumentQuerySource**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigDocumentQuerySource.md) |  |  [optional] |
|**knowledgeBaseQuerySource** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigKnowledgeBaseQuerySource**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigKnowledgeBaseQuerySource.md) |  |  [optional] |
|**maxResults** | **Integer** | Maximum number of results to return. Currently, if unset, defaults to 10. And the max number is 20. |  [optional] |
|**sections** | [**GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigSections**](GoogleCloudDialogflowV2beta1HumanAgentAssistantConfigSuggestionQueryConfigSections.md) |  |  [optional] |



