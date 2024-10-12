# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1ArticleSuggestionData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceScore** | **Number** | The system&#39;s confidence score that this article is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain). | [optional] 
**metadata** | **{String: String}** | Map that contains metadata about the Article Suggestion and the document that it originates from. | [optional] 
**queryRecord** | **String** | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record} | [optional] 
**source** | **String** | The knowledge document that this answer was extracted from. Format: projects/{project}/knowledgeBases/{knowledge_base}/documents/{document} | [optional] 
**title** | **String** | Article title. | [optional] 
**uri** | **String** | Article URI. | [optional] 


