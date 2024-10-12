# VertexAiApi.LearningGenaiRootCodeyCheckpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codeyTruncatorMetadata** | [**LearningGenaiRootCodeyTruncatorMetadata**](LearningGenaiRootCodeyTruncatorMetadata.md) |  | [optional] 
**currentSample** | **String** | Current state of the sample after truncator. | [optional] 
**postInferenceStep** | **String** | Postprocessor run that yielded this checkpoint. | [optional] 



## Enum: PostInferenceStepEnum


* `POST_PROCESSING_STEP_UNSPECIFIED` (value: `"STEP_POST_PROCESSING_STEP_UNSPECIFIED"`)

* `ORIGINAL_MODEL_OUTPUT` (value: `"STEP_ORIGINAL_MODEL_OUTPUT"`)

* `MODEL_OUTPUT_DEDUPLICATION` (value: `"STEP_MODEL_OUTPUT_DEDUPLICATION"`)

* `STOP_SEQUENCE_TRUNCATION` (value: `"STEP_STOP_SEQUENCE_TRUNCATION"`)

* `HEURISTIC_TRUNCATION` (value: `"STEP_HEURISTIC_TRUNCATION"`)

* `WALD_TRUNCATION` (value: `"STEP_WALD_TRUNCATION"`)

* `WHITESPACE_TRUNCATION` (value: `"STEP_WHITESPACE_TRUNCATION"`)

* `FINAL_DEDUPLICATION` (value: `"STEP_FINAL_DEDUPLICATION"`)

* `TOXICITY_CHECK` (value: `"STEP_TOXICITY_CHECK"`)

* `RECITATION_CHECK` (value: `"STEP_RECITATION_CHECK"`)

* `RETURNED` (value: `"STEP_RETURNED"`)

* `WALKBACK_CORRECTION` (value: `"STEP_WALKBACK_CORRECTION"`)

* `SCORE_THRESHOLDING` (value: `"STEP_SCORE_THRESHOLDING"`)

* `MODEL_CONFIG_STOP_SEQUENCE_TRUNCATION` (value: `"STEP_MODEL_CONFIG_STOP_SEQUENCE_TRUNCATION"`)

* `CUSTOM_STOP_SEQUENCE_TRUNCATION` (value: `"STEP_CUSTOM_STOP_SEQUENCE_TRUNCATION"`)

* `EXPECTED_SAMPLE_SIZE` (value: `"STEP_EXPECTED_SAMPLE_SIZE"`)




