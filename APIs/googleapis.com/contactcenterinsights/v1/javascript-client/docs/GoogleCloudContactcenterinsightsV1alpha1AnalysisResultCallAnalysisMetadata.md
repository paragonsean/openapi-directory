# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1AnalysisResultCallAnalysisMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**[GoogleCloudContactcenterinsightsV1alpha1CallAnnotation]**](GoogleCloudContactcenterinsightsV1alpha1CallAnnotation.md) | A list of call annotations that apply to this call. | [optional] 
**entities** | [**{String: GoogleCloudContactcenterinsightsV1alpha1Entity}**](GoogleCloudContactcenterinsightsV1alpha1Entity.md) | All the entities in the call. | [optional] 
**intents** | [**{String: GoogleCloudContactcenterinsightsV1alpha1Intent}**](GoogleCloudContactcenterinsightsV1alpha1Intent.md) | All the matched intents in the call. | [optional] 
**issueModelResult** | [**GoogleCloudContactcenterinsightsV1alpha1IssueModelResult**](GoogleCloudContactcenterinsightsV1alpha1IssueModelResult.md) |  | [optional] 
**phraseMatchers** | [**{String: GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData}**](GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData.md) | All the matched phrase matchers in the call. | [optional] 
**sentiments** | [**[GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment]**](GoogleCloudContactcenterinsightsV1alpha1ConversationLevelSentiment.md) | Overall conversation-level sentiment for each channel of the call. | [optional] 


