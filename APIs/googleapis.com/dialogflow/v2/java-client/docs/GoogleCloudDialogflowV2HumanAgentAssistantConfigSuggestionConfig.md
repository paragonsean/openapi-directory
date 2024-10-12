

# GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionConfig

Detail human agent assistant config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**featureConfigs** | [**List&lt;GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig&gt;**](GoogleCloudDialogflowV2HumanAgentAssistantConfigSuggestionFeatureConfig.md) | Configuration of different suggestion features. One feature can have only one config. |  [optional] |
|**groupSuggestionResponses** | **Boolean** | If &#x60;group_suggestion_responses&#x60; is false, and there are multiple &#x60;feature_configs&#x60; in &#x60;event based suggestion&#x60; or StreamingAnalyzeContent, we will try to deliver suggestions to customers as soon as we get new suggestion. Different type of suggestions based on the same context will be in separate Pub/Sub event or &#x60;StreamingAnalyzeContentResponse&#x60;. If &#x60;group_suggestion_responses&#x60; set to true. All the suggestions to the same participant based on the same context will be grouped into a single Pub/Sub event or StreamingAnalyzeContentResponse. |  [optional] |



