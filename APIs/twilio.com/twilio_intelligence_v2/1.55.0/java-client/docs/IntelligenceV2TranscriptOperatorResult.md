

# IntelligenceV2TranscriptOperatorResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extractMatch** | **Boolean** | Boolean to tell if extract Language Understanding Processing model matches results. |  [optional] |
|**extractResults** | **Object** | List of text extraction results. This might be available on classify-extract model outputs. |  [optional] |
|**labelProbabilities** | **Object** | The labels probabilities. This might be available on conversation classify model outputs. |  [optional] |
|**matchProbability** | **BigDecimal** | Percentage of &#39;matching&#39; class needed to consider a sentence matches |  [optional] |
|**name** | **String** | The name of the applied Language Understanding. |  [optional] |
|**normalizedResult** | **String** | Normalized output of extraction stage which matches Label. |  [optional] |
|**operatorSid** | **String** | A 34 character string that identifies this Language Understanding operator sid. |  [optional] |
|**operatorType** | **OperatorResultEnumOperatorType** |  |  [optional] |
|**predictedLabel** | **String** | The &#39;matching&#39; class. This might be available on conversation classify model outputs. |  [optional] |
|**predictedProbability** | **BigDecimal** | Percentage of &#39;matching&#39; class needed to consider a sentence matches. |  [optional] |
|**textGenerationResults** | **Object** | Output of a text generation operator for example Conversation Sumamary. |  [optional] |
|**transcriptSid** | **String** | A 34 character string that uniquely identifies this Transcript. |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |
|**utteranceMatch** | **Boolean** | Boolean to tell if Utterance matches results. |  [optional] |
|**utteranceResults** | **List&lt;Object&gt;** | List of mapped utterance object which matches sentences. |  [optional] |



