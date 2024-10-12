

# GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata

Call-specific metadata created during analysis.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | [**List&lt;GoogleCloudContactcenterinsightsV1CallAnnotation&gt;**](GoogleCloudContactcenterinsightsV1CallAnnotation.md) | A list of call annotations that apply to this call. |  [optional] |
|**entities** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1Entity&gt;**](GoogleCloudContactcenterinsightsV1Entity.md) | All the entities in the call. |  [optional] |
|**intents** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1Intent&gt;**](GoogleCloudContactcenterinsightsV1Intent.md) | All the matched intents in the call. |  [optional] |
|**issueModelResult** | [**GoogleCloudContactcenterinsightsV1IssueModelResult**](GoogleCloudContactcenterinsightsV1IssueModelResult.md) |  |  [optional] |
|**phraseMatchers** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1PhraseMatchData&gt;**](GoogleCloudContactcenterinsightsV1PhraseMatchData.md) | All the matched phrase matchers in the call. |  [optional] |
|**sentiments** | [**List&lt;GoogleCloudContactcenterinsightsV1ConversationLevelSentiment&gt;**](GoogleCloudContactcenterinsightsV1ConversationLevelSentiment.md) | Overall conversation-level sentiment for each channel of the call. |  [optional] |



