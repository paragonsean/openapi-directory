# VertexAiApi.CloudAiNlLlmProtoServiceCandidate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**citationMetadata** | [**CloudAiNlLlmProtoServiceCitationMetadata**](CloudAiNlLlmProtoServiceCitationMetadata.md) |  | [optional] 
**content** | [**CloudAiNlLlmProtoServiceContent**](CloudAiNlLlmProtoServiceContent.md) |  | [optional] 
**finishMessage** | **String** | A string that describes the filtering behavior in more detail. Only filled when reason is set. | [optional] 
**finishReason** | **String** | The reason why the model stopped generating tokens. | [optional] 
**groundingMetadata** | [**LearningGenaiRootGroundingMetadata**](LearningGenaiRootGroundingMetadata.md) |  | [optional] 
**index** | **Number** | Index of the candidate. | [optional] 
**safetyRatings** | [**[CloudAiNlLlmProtoServiceSafetyRating]**](CloudAiNlLlmProtoServiceSafetyRating.md) | Safety ratings of the generated content. | [optional] 



## Enum: FinishReasonEnum


* `UNSPECIFIED` (value: `"FINISH_REASON_UNSPECIFIED"`)

* `STOP` (value: `"FINISH_REASON_STOP"`)

* `MAX_TOKENS` (value: `"FINISH_REASON_MAX_TOKENS"`)

* `SAFETY` (value: `"FINISH_REASON_SAFETY"`)

* `RECITATION` (value: `"FINISH_REASON_RECITATION"`)

* `OTHER` (value: `"FINISH_REASON_OTHER"`)




