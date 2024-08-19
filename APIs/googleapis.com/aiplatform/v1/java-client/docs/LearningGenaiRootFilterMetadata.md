

# LearningGenaiRootFilterMetadata


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | [**ConfidenceEnum**](#ConfidenceEnum) | Filter confidence. |  [optional] |
|**debugInfo** | [**LearningGenaiRootFilterMetadataFilterDebugInfo**](LearningGenaiRootFilterMetadataFilterDebugInfo.md) |  |  [optional] |
|**fallback** | **String** | A fallback message chosen by the applied filter. |  [optional] |
|**info** | **String** | Additional info for the filter. |  [optional] |
|**name** | **String** | Name of the filter that triggered. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Filter reason. |  [optional] |
|**text** | **String** | The input query or generated response that is getting filtered. |  [optional] |



## Enum: ConfidenceEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;FILTER_CONFIDENCE_UNKNOWN&quot; |
| VERY_LOW | &quot;FILTER_CONFIDENCE_VERY_LOW&quot; |
| LOW | &quot;FILTER_CONFIDENCE_LOW&quot; |
| MEDIUM | &quot;FILTER_CONFIDENCE_MEDIUM&quot; |
| HIGH | &quot;FILTER_CONFIDENCE_HIGH&quot; |
| VERY_HIGH | &quot;FILTER_CONFIDENCE_VERY_HIGH&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;FILTER_REASON_UNKNOWN&quot; |
| NOT_FILTERED | &quot;FILTER_REASON_NOT_FILTERED&quot; |
| SENSITIVE | &quot;FILTER_REASON_SENSITIVE&quot; |
| RECITATION | &quot;FILTER_REASON_RECITATION&quot; |
| LANGUAGE | &quot;FILTER_REASON_LANGUAGE&quot; |
| TAKEDOWN | &quot;FILTER_REASON_TAKEDOWN&quot; |
| CLASSIFIER | &quot;FILTER_REASON_CLASSIFIER&quot; |
| EMPTY_RESPONSE | &quot;FILTER_REASON_EMPTY_RESPONSE&quot; |
| SIMILARITY_TAKEDOWN | &quot;FILTER_REASON_SIMILARITY_TAKEDOWN&quot; |
| UNSAFE | &quot;FILTER_REASON_UNSAFE&quot; |
| PAIRWISE_CLASSIFIER | &quot;FILTER_REASON_PAIRWISE_CLASSIFIER&quot; |
| CODEY | &quot;FILTER_REASON_CODEY&quot; |
| URL | &quot;FILTER_REASON_URL&quot; |
| EMAIL | &quot;FILTER_REASON_EMAIL&quot; |
| SAFETY_CAT | &quot;FILTER_REASON_SAFETY_CAT&quot; |
| REQUEST_RESPONSE_TAKEDOWN | &quot;FILTER_REASON_REQUEST_RESPONSE_TAKEDOWN&quot; |
| RAI_PQC | &quot;FILTER_REASON_RAI_PQC&quot; |
| ATLAS | &quot;FILTER_REASON_ATLAS&quot; |
| RAI_CSAM | &quot;FILTER_REASON_RAI_CSAM&quot; |
| RAI_FRINGE | &quot;FILTER_REASON_RAI_FRINGE&quot; |
| RAI_SPII | &quot;FILTER_REASON_RAI_SPII&quot; |
| RAI_IMAGE_VIOLENCE | &quot;FILTER_REASON_RAI_IMAGE_VIOLENCE&quot; |
| RAI_IMAGE_PORN | &quot;FILTER_REASON_RAI_IMAGE_PORN&quot; |
| RAI_IMAGE_CSAM | &quot;FILTER_REASON_RAI_IMAGE_CSAM&quot; |
| RAI_IMAGE_PEDO | &quot;FILTER_REASON_RAI_IMAGE_PEDO&quot; |
| RAI_VIDEO_FRAME_VIOLENCE | &quot;FILTER_REASON_RAI_VIDEO_FRAME_VIOLENCE&quot; |
| RAI_VIDEO_FRAME_PORN | &quot;FILTER_REASON_RAI_VIDEO_FRAME_PORN&quot; |
| RAI_VIDEO_FRAME_CSAM | &quot;FILTER_REASON_RAI_VIDEO_FRAME_CSAM&quot; |
| RAI_VIDEO_FRAME_PEDO | &quot;FILTER_REASON_RAI_VIDEO_FRAME_PEDO&quot; |
| RAI_CONTEXTUAL_DANGEROUS | &quot;FILTER_REASON_RAI_CONTEXTUAL_DANGEROUS&quot; |
| RAI_GRAIL_TEXT | &quot;FILTER_REASON_RAI_GRAIL_TEXT&quot; |
| RAI_GRAIL_IMAGE | &quot;FILTER_REASON_RAI_GRAIL_IMAGE&quot; |
| RAI_SAFETYCAT | &quot;FILTER_REASON_RAI_SAFETYCAT&quot; |
| TOXICITY | &quot;FILTER_REASON_TOXICITY&quot; |
| ATLAS_PRICING | &quot;FILTER_REASON_ATLAS_PRICING&quot; |
| ATLAS_BILLING | &quot;FILTER_REASON_ATLAS_BILLING&quot; |
| ATLAS_NON_ENGLISH_QUESTION | &quot;FILTER_REASON_ATLAS_NON_ENGLISH_QUESTION&quot; |
| ATLAS_NOT_RELATED_TO_GCP | &quot;FILTER_REASON_ATLAS_NOT_RELATED_TO_GCP&quot; |
| ATLAS_AWS_AZURE_RELATED | &quot;FILTER_REASON_ATLAS_AWS_AZURE_RELATED&quot; |



