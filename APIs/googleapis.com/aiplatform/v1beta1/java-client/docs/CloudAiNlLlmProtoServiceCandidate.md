

# CloudAiNlLlmProtoServiceCandidate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**citationMetadata** | [**CloudAiNlLlmProtoServiceCitationMetadata**](CloudAiNlLlmProtoServiceCitationMetadata.md) |  |  [optional] |
|**content** | [**CloudAiNlLlmProtoServiceContent**](CloudAiNlLlmProtoServiceContent.md) |  |  [optional] |
|**finishMessage** | **String** | A string that describes the filtering behavior in more detail. Only filled when reason is set. |  [optional] |
|**finishReason** | [**FinishReasonEnum**](#FinishReasonEnum) | The reason why the model stopped generating tokens. |  [optional] |
|**groundingMetadata** | [**LearningGenaiRootGroundingMetadata**](LearningGenaiRootGroundingMetadata.md) |  |  [optional] |
|**index** | **Integer** | Index of the candidate. |  [optional] |
|**safetyRatings** | [**List&lt;CloudAiNlLlmProtoServiceSafetyRating&gt;**](CloudAiNlLlmProtoServiceSafetyRating.md) | Safety ratings of the generated content. |  [optional] |



## Enum: FinishReasonEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FINISH_REASON_UNSPECIFIED&quot; |
| STOP | &quot;FINISH_REASON_STOP&quot; |
| MAX_TOKENS | &quot;FINISH_REASON_MAX_TOKENS&quot; |
| SAFETY | &quot;FINISH_REASON_SAFETY&quot; |
| RECITATION | &quot;FINISH_REASON_RECITATION&quot; |
| OTHER | &quot;FINISH_REASON_OTHER&quot; |



