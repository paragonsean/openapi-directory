# DialogflowApi.GoogleCloudDialogflowV2beta1SuggestionFaqAnswer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **String** | Output only. The piece of text from the &#x60;source&#x60; knowledge base document. | [optional] 
**answerRecord** | **String** | Output only. The name of answer record, in the format of \&quot;projects//locations//answerRecords/\&quot; | [optional] 
**confidence** | **Number** | The system&#39;s confidence score that this Knowledge answer is a good match for this conversational query, range from 0.0 (completely uncertain) to 1.0 (completely certain). | [optional] 
**metadata** | **{String: String}** | Output only. A map that contains metadata about the answer and the document from which it originates. | [optional] 
**question** | **String** | Output only. The corresponding FAQ question. | [optional] 
**source** | **String** | Output only. Indicates which Knowledge Document this answer was extracted from. Format: &#x60;projects//locations//agent/knowledgeBases//documents/&#x60;. | [optional] 


