# VertexAiApi.LearningGenaiRootFilterMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **String** | Filter confidence. | [optional] 
**debugInfo** | [**LearningGenaiRootFilterMetadataFilterDebugInfo**](LearningGenaiRootFilterMetadataFilterDebugInfo.md) |  | [optional] 
**fallback** | **String** | A fallback message chosen by the applied filter. | [optional] 
**info** | **String** | Additional info for the filter. | [optional] 
**name** | **String** | Name of the filter that triggered. | [optional] 
**reason** | **String** | Filter reason. | [optional] 
**text** | **String** | The input query or generated response that is getting filtered. | [optional] 



## Enum: ConfidenceEnum


* `UNKNOWN` (value: `"FILTER_CONFIDENCE_UNKNOWN"`)

* `VERY_LOW` (value: `"FILTER_CONFIDENCE_VERY_LOW"`)

* `LOW` (value: `"FILTER_CONFIDENCE_LOW"`)

* `MEDIUM` (value: `"FILTER_CONFIDENCE_MEDIUM"`)

* `HIGH` (value: `"FILTER_CONFIDENCE_HIGH"`)

* `VERY_HIGH` (value: `"FILTER_CONFIDENCE_VERY_HIGH"`)





## Enum: ReasonEnum


* `UNKNOWN` (value: `"FILTER_REASON_UNKNOWN"`)

* `NOT_FILTERED` (value: `"FILTER_REASON_NOT_FILTERED"`)

* `SENSITIVE` (value: `"FILTER_REASON_SENSITIVE"`)

* `RECITATION` (value: `"FILTER_REASON_RECITATION"`)

* `LANGUAGE` (value: `"FILTER_REASON_LANGUAGE"`)

* `TAKEDOWN` (value: `"FILTER_REASON_TAKEDOWN"`)

* `CLASSIFIER` (value: `"FILTER_REASON_CLASSIFIER"`)

* `EMPTY_RESPONSE` (value: `"FILTER_REASON_EMPTY_RESPONSE"`)

* `SIMILARITY_TAKEDOWN` (value: `"FILTER_REASON_SIMILARITY_TAKEDOWN"`)

* `UNSAFE` (value: `"FILTER_REASON_UNSAFE"`)

* `PAIRWISE_CLASSIFIER` (value: `"FILTER_REASON_PAIRWISE_CLASSIFIER"`)

* `CODEY` (value: `"FILTER_REASON_CODEY"`)

* `URL` (value: `"FILTER_REASON_URL"`)

* `EMAIL` (value: `"FILTER_REASON_EMAIL"`)

* `SAFETY_CAT` (value: `"FILTER_REASON_SAFETY_CAT"`)

* `REQUEST_RESPONSE_TAKEDOWN` (value: `"FILTER_REASON_REQUEST_RESPONSE_TAKEDOWN"`)

* `RAI_PQC` (value: `"FILTER_REASON_RAI_PQC"`)

* `ATLAS` (value: `"FILTER_REASON_ATLAS"`)

* `RAI_CSAM` (value: `"FILTER_REASON_RAI_CSAM"`)

* `RAI_FRINGE` (value: `"FILTER_REASON_RAI_FRINGE"`)

* `RAI_SPII` (value: `"FILTER_REASON_RAI_SPII"`)

* `RAI_IMAGE_VIOLENCE` (value: `"FILTER_REASON_RAI_IMAGE_VIOLENCE"`)

* `RAI_IMAGE_PORN` (value: `"FILTER_REASON_RAI_IMAGE_PORN"`)

* `RAI_IMAGE_CSAM` (value: `"FILTER_REASON_RAI_IMAGE_CSAM"`)

* `RAI_IMAGE_PEDO` (value: `"FILTER_REASON_RAI_IMAGE_PEDO"`)

* `RAI_VIDEO_FRAME_VIOLENCE` (value: `"FILTER_REASON_RAI_VIDEO_FRAME_VIOLENCE"`)

* `RAI_VIDEO_FRAME_PORN` (value: `"FILTER_REASON_RAI_VIDEO_FRAME_PORN"`)

* `RAI_VIDEO_FRAME_CSAM` (value: `"FILTER_REASON_RAI_VIDEO_FRAME_CSAM"`)

* `RAI_VIDEO_FRAME_PEDO` (value: `"FILTER_REASON_RAI_VIDEO_FRAME_PEDO"`)

* `RAI_CONTEXTUAL_DANGEROUS` (value: `"FILTER_REASON_RAI_CONTEXTUAL_DANGEROUS"`)

* `RAI_GRAIL_TEXT` (value: `"FILTER_REASON_RAI_GRAIL_TEXT"`)

* `RAI_GRAIL_IMAGE` (value: `"FILTER_REASON_RAI_GRAIL_IMAGE"`)

* `RAI_SAFETYCAT` (value: `"FILTER_REASON_RAI_SAFETYCAT"`)

* `TOXICITY` (value: `"FILTER_REASON_TOXICITY"`)

* `ATLAS_PRICING` (value: `"FILTER_REASON_ATLAS_PRICING"`)

* `ATLAS_BILLING` (value: `"FILTER_REASON_ATLAS_BILLING"`)

* `ATLAS_NON_ENGLISH_QUESTION` (value: `"FILTER_REASON_ATLAS_NON_ENGLISH_QUESTION"`)

* `ATLAS_NOT_RELATED_TO_GCP` (value: `"FILTER_REASON_ATLAS_NOT_RELATED_TO_GCP"`)

* `ATLAS_AWS_AZURE_RELATED` (value: `"FILTER_REASON_ATLAS_AWS_AZURE_RELATED"`)




