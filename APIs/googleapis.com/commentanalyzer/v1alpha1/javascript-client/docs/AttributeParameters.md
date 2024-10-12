# PerspectiveCommentAnalyzerApi.AttributeParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scoreThreshold** | **Number** | Don&#39;t return scores for this attribute that are below this threshold. If unset, a default threshold will be applied. A FloatValue wrapper is used to distinguish between 0 vs. default/unset. | [optional] 
**scoreType** | **String** | What type of scores to return. If unset, defaults to probability scores. | [optional] 



## Enum: ScoreTypeEnum


* `SCORE_TYPE_UNSPECIFIED` (value: `"SCORE_TYPE_UNSPECIFIED"`)

* `PROBABILITY` (value: `"PROBABILITY"`)

* `STD_DEV_SCORE` (value: `"STD_DEV_SCORE"`)

* `PERCENTILE` (value: `"PERCENTILE"`)

* `RAW` (value: `"RAW"`)




