# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1AnalysisResultCallAnalysisMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**[GoogleCloudContactcenterinsightsV1CallAnnotation]**](GoogleCloudContactcenterinsightsV1CallAnnotation.md) | A list of call annotations that apply to this call. | [optional] 
**entities** | [**{String: GoogleCloudContactcenterinsightsV1Entity}**](GoogleCloudContactcenterinsightsV1Entity.md) | All the entities in the call. | [optional] 
**intents** | [**{String: GoogleCloudContactcenterinsightsV1Intent}**](GoogleCloudContactcenterinsightsV1Intent.md) | All the matched intents in the call. | [optional] 
**issueModelResult** | [**GoogleCloudContactcenterinsightsV1IssueModelResult**](GoogleCloudContactcenterinsightsV1IssueModelResult.md) |  | [optional] 
**phraseMatchers** | [**{String: GoogleCloudContactcenterinsightsV1PhraseMatchData}**](GoogleCloudContactcenterinsightsV1PhraseMatchData.md) | All the matched phrase matchers in the call. | [optional] 
**sentiments** | [**[GoogleCloudContactcenterinsightsV1ConversationLevelSentiment]**](GoogleCloudContactcenterinsightsV1ConversationLevelSentiment.md) | Overall conversation-level sentiment for each channel of the call. | [optional] 


