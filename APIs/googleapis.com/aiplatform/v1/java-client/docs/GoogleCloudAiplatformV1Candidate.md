

# GoogleCloudAiplatformV1Candidate

A response candidate generated from the model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**citationMetadata** | [**GoogleCloudAiplatformV1CitationMetadata**](GoogleCloudAiplatformV1CitationMetadata.md) |  |  [optional] |
|**content** | [**GoogleCloudAiplatformV1Content**](GoogleCloudAiplatformV1Content.md) |  |  [optional] |
|**finishMessage** | **String** | Output only. Describes the reason the mode stopped generating tokens in more detail. This is only filled when &#x60;finish_reason&#x60; is set. |  [optional] [readonly] |
|**finishReason** | [**FinishReasonEnum**](#FinishReasonEnum) | Output only. The reason why the model stopped generating tokens. If empty, the model has not stopped generating the tokens. |  [optional] [readonly] |
|**groundingMetadata** | [**GoogleCloudAiplatformV1GroundingMetadata**](GoogleCloudAiplatformV1GroundingMetadata.md) |  |  [optional] |
|**index** | **Integer** | Output only. Index of the candidate. |  [optional] [readonly] |
|**safetyRatings** | [**List&lt;GoogleCloudAiplatformV1SafetyRating&gt;**](GoogleCloudAiplatformV1SafetyRating.md) | Output only. List of ratings for the safety of a response candidate. There is at most one rating per category. |  [optional] [readonly] |



## Enum: FinishReasonEnum

| Name | Value |
|---- | -----|
| FINISH_REASON_UNSPECIFIED | &quot;FINISH_REASON_UNSPECIFIED&quot; |
| STOP | &quot;STOP&quot; |
| MAX_TOKENS | &quot;MAX_TOKENS&quot; |
| SAFETY | &quot;SAFETY&quot; |
| RECITATION | &quot;RECITATION&quot; |
| OTHER | &quot;OTHER&quot; |



