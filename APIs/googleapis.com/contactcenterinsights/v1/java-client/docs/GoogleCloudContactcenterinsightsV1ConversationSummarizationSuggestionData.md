

# GoogleCloudContactcenterinsightsV1ConversationSummarizationSuggestionData

Conversation summarization suggestion data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerRecord** | **String** | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record} |  [optional] |
|**confidence** | **Float** | The confidence score of the summarization. |  [optional] |
|**conversationModel** | **String** | The name of the model that generates this summary. Format: projects/{project}/locations/{location}/conversationModels/{conversation_model} |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | A map that contains metadata about the summarization and the document from which it originates. |  [optional] |
|**text** | **String** | The summarization content that is concatenated into one string. |  [optional] |
|**textSections** | **Map&lt;String, String&gt;** | The summarization content that is divided into sections. The key is the section&#39;s name and the value is the section&#39;s content. There is no specific format for the key or value. |  [optional] |



