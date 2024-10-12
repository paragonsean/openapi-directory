

# GoogleCloudContactcenterinsightsV1alpha1FaqAnswerData

Agent Assist frequently-asked-question answer data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answer** | **String** | The piece of text from the &#x60;source&#x60; knowledge base document. |  [optional] |
|**confidenceScore** | **Float** | The system&#39;s confidence score that this answer is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain). |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Map that contains metadata about the FAQ answer and the document that it originates from. |  [optional] |
|**queryRecord** | **String** | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record} |  [optional] |
|**question** | **String** | The corresponding FAQ question. |  [optional] |
|**source** | **String** | The knowledge document that this answer was extracted from. Format: projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}. |  [optional] |



