

# GoogleCloudDialogflowV2FaqAnswer

Represents answer from \"frequently asked questions\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answer** | **String** | The piece of text from the &#x60;source&#x60; knowledge base document. |  [optional] |
|**answerRecord** | **String** | The name of answer record, in the format of \&quot;projects//locations//answerRecords/\&quot; |  [optional] |
|**confidence** | **Float** | The system&#39;s confidence score that this Knowledge answer is a good match for this conversational query, range from 0.0 (completely uncertain) to 1.0 (completely certain). |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | A map that contains metadata about the answer and the document from which it originates. |  [optional] |
|**question** | **String** | The corresponding FAQ question. |  [optional] |
|**source** | **String** | Indicates which Knowledge Document this answer was extracted from. Format: &#x60;projects//locations//agent/knowledgeBases//documents/&#x60;. |  [optional] |



