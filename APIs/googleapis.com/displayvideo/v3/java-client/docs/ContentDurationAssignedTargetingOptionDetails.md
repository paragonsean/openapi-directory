

# ContentDurationAssignedTargetingOptionDetails

Details for content duration assigned targeting option. This will be populated in the content_duration_details field when targeting_type is `TARGETING_TYPE_CONTENT_DURATION`. Explicitly targeting all options is not supported. Remove all content duration targeting options to achieve this effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentDuration** | [**ContentDurationEnum**](#ContentDurationEnum) | Output only. The content duration. |  [optional] [readonly] |
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_CONTENT_DURATION&#x60;. |  [optional] |



## Enum: ContentDurationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONTENT_DURATION_UNSPECIFIED&quot; |
| UNKNOWN | &quot;CONTENT_DURATION_UNKNOWN&quot; |
| _0_TO_1_MIN | &quot;CONTENT_DURATION_0_TO_1_MIN&quot; |
| _1_TO_5_MIN | &quot;CONTENT_DURATION_1_TO_5_MIN&quot; |
| _5_TO_15_MIN | &quot;CONTENT_DURATION_5_TO_15_MIN&quot; |
| _15_TO_30_MIN | &quot;CONTENT_DURATION_15_TO_30_MIN&quot; |
| _30_TO_60_MIN | &quot;CONTENT_DURATION_30_TO_60_MIN&quot; |
| OVER_60_MIN | &quot;CONTENT_DURATION_OVER_60_MIN&quot; |



