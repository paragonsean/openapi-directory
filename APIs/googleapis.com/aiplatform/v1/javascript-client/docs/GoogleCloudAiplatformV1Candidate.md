# VertexAiApi.GoogleCloudAiplatformV1Candidate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**citationMetadata** | [**GoogleCloudAiplatformV1CitationMetadata**](GoogleCloudAiplatformV1CitationMetadata.md) |  | [optional] 
**content** | [**GoogleCloudAiplatformV1Content**](GoogleCloudAiplatformV1Content.md) |  | [optional] 
**finishMessage** | **String** | Output only. Describes the reason the mode stopped generating tokens in more detail. This is only filled when &#x60;finish_reason&#x60; is set. | [optional] [readonly] 
**finishReason** | **String** | Output only. The reason why the model stopped generating tokens. If empty, the model has not stopped generating the tokens. | [optional] [readonly] 
**groundingMetadata** | [**GoogleCloudAiplatformV1GroundingMetadata**](GoogleCloudAiplatformV1GroundingMetadata.md) |  | [optional] 
**index** | **Number** | Output only. Index of the candidate. | [optional] [readonly] 
**safetyRatings** | [**[GoogleCloudAiplatformV1SafetyRating]**](GoogleCloudAiplatformV1SafetyRating.md) | Output only. List of ratings for the safety of a response candidate. There is at most one rating per category. | [optional] [readonly] 



## Enum: FinishReasonEnum


* `FINISH_REASON_UNSPECIFIED` (value: `"FINISH_REASON_UNSPECIFIED"`)

* `STOP` (value: `"STOP"`)

* `MAX_TOKENS` (value: `"MAX_TOKENS"`)

* `SAFETY` (value: `"SAFETY"`)

* `RECITATION` (value: `"RECITATION"`)

* `OTHER` (value: `"OTHER"`)




