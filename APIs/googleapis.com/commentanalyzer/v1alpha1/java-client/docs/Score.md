

# Score

Analysis scores are described by a value and a ScoreType.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of the above value. |  [optional] |
|**value** | **Float** | Score value. Semantics described by type below. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SCORE_TYPE_UNSPECIFIED | &quot;SCORE_TYPE_UNSPECIFIED&quot; |
| PROBABILITY | &quot;PROBABILITY&quot; |
| STD_DEV_SCORE | &quot;STD_DEV_SCORE&quot; |
| PERCENTILE | &quot;PERCENTILE&quot; |
| RAW | &quot;RAW&quot; |



