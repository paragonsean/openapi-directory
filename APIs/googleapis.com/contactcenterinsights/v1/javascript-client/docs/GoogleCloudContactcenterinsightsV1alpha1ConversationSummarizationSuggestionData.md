# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1ConversationSummarizationSuggestionData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answerRecord** | **String** | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record} | [optional] 
**confidence** | **Number** | The confidence score of the summarization. | [optional] 
**conversationModel** | **String** | The name of the model that generates this summary. Format: projects/{project}/locations/{location}/conversationModels/{conversation_model} | [optional] 
**metadata** | **{String: String}** | A map that contains metadata about the summarization and the document from which it originates. | [optional] 
**text** | **String** | The summarization content that is concatenated into one string. | [optional] 
**textSections** | **{String: String}** | The summarization content that is divided into sections. The key is the section&#39;s name and the value is the section&#39;s content. There is no specific format for the key or value. | [optional] 


