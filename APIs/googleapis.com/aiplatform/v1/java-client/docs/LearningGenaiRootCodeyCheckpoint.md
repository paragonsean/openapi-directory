

# LearningGenaiRootCodeyCheckpoint

Describes a sample at a checkpoint for post-processing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeyTruncatorMetadata** | [**LearningGenaiRootCodeyTruncatorMetadata**](LearningGenaiRootCodeyTruncatorMetadata.md) |  |  [optional] |
|**currentSample** | **String** | Current state of the sample after truncator. |  [optional] |
|**postInferenceStep** | [**PostInferenceStepEnum**](#PostInferenceStepEnum) | Postprocessor run that yielded this checkpoint. |  [optional] |



## Enum: PostInferenceStepEnum

| Name | Value |
|---- | -----|
| POST_PROCESSING_STEP_UNSPECIFIED | &quot;STEP_POST_PROCESSING_STEP_UNSPECIFIED&quot; |
| ORIGINAL_MODEL_OUTPUT | &quot;STEP_ORIGINAL_MODEL_OUTPUT&quot; |
| MODEL_OUTPUT_DEDUPLICATION | &quot;STEP_MODEL_OUTPUT_DEDUPLICATION&quot; |
| STOP_SEQUENCE_TRUNCATION | &quot;STEP_STOP_SEQUENCE_TRUNCATION&quot; |
| HEURISTIC_TRUNCATION | &quot;STEP_HEURISTIC_TRUNCATION&quot; |
| WALD_TRUNCATION | &quot;STEP_WALD_TRUNCATION&quot; |
| WHITESPACE_TRUNCATION | &quot;STEP_WHITESPACE_TRUNCATION&quot; |
| FINAL_DEDUPLICATION | &quot;STEP_FINAL_DEDUPLICATION&quot; |
| TOXICITY_CHECK | &quot;STEP_TOXICITY_CHECK&quot; |
| RECITATION_CHECK | &quot;STEP_RECITATION_CHECK&quot; |
| RETURNED | &quot;STEP_RETURNED&quot; |
| WALKBACK_CORRECTION | &quot;STEP_WALKBACK_CORRECTION&quot; |
| SCORE_THRESHOLDING | &quot;STEP_SCORE_THRESHOLDING&quot; |
| MODEL_CONFIG_STOP_SEQUENCE_TRUNCATION | &quot;STEP_MODEL_CONFIG_STOP_SEQUENCE_TRUNCATION&quot; |
| CUSTOM_STOP_SEQUENCE_TRUNCATION | &quot;STEP_CUSTOM_STOP_SEQUENCE_TRUNCATION&quot; |
| EXPECTED_SAMPLE_SIZE | &quot;STEP_EXPECTED_SAMPLE_SIZE&quot; |



