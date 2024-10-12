

# GoogleCloudContactcenterinsightsV1alpha1AnalysisResultCallAnalysisMetadata

Call-specific metadata created during analysis.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | [**List&lt;GoogleCloudContactcenterinsightsV1alpha1CallAnnotation&gt;**](GoogleCloudContactcenterinsightsV1alpha1CallAnnotation.md) | A list of call annotations that apply to this call. |  [optional] |
|**entities** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1alpha1Entity&gt;**](GoogleCloudContactcenterinsightsV1alpha1Entity.md) | All the entities in the call. |  [optional] |
|**intents** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1alpha1Intent&gt;**](GoogleCloudContactcenterinsightsV1alpha1Intent.md) | All the matched intents in the call. |  [optional] |
|**issueModelResult** | [**GoogleCloudContactcenterinsightsV1alpha1IssueModelResult**](GoogleCloudContactcenterinsightsV1alpha1IssueModelResult.md) |  |  [optional] |
|**phraseMatchers** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData&gt;**](GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData.md) | All the matched phrase matchers in the call. |  [optional] |
|**sentiments** | [**List&lt;GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment&gt;**](GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment.md) | Overall conversation-level sentiment for each channel of the call. |  [optional] |



