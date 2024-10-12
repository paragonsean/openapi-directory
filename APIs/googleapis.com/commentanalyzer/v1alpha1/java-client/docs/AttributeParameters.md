

# AttributeParameters

Configurable parameters for attribute scoring.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scoreThreshold** | **Float** | Don&#39;t return scores for this attribute that are below this threshold. If unset, a default threshold will be applied. A FloatValue wrapper is used to distinguish between 0 vs. default/unset. |  [optional] |
|**scoreType** | [**ScoreTypeEnum**](#ScoreTypeEnum) | What type of scores to return. If unset, defaults to probability scores. |  [optional] |



## Enum: ScoreTypeEnum

| Name | Value |
|---- | -----|
| SCORE_TYPE_UNSPECIFIED | &quot;SCORE_TYPE_UNSPECIFIED&quot; |
| PROBABILITY | &quot;PROBABILITY&quot; |
| STD_DEV_SCORE | &quot;STD_DEV_SCORE&quot; |
| PERCENTILE | &quot;PERCENTILE&quot; |
| RAW | &quot;RAW&quot; |



