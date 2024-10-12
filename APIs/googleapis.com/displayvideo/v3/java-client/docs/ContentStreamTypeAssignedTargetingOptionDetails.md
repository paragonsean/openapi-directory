

# ContentStreamTypeAssignedTargetingOptionDetails

Details for content stream type assigned targeting option. This will be populated in the content_stream_type_details field when targeting_type is `TARGETING_TYPE_CONTENT_STREAM_TYPE`. Explicitly targeting all options is not supported. Remove all content stream type targeting options to achieve this effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentStreamType** | [**ContentStreamTypeEnum**](#ContentStreamTypeEnum) | Output only. The content stream type. |  [optional] [readonly] |
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_CONTENT_STREAM_TYPE&#x60;. |  [optional] |



## Enum: ContentStreamTypeEnum

| Name | Value |
|---- | -----|
| STREAM_TYPE_UNSPECIFIED | &quot;CONTENT_STREAM_TYPE_UNSPECIFIED&quot; |
| LIVE_STREAM | &quot;CONTENT_LIVE_STREAM&quot; |
| ON_DEMAND | &quot;CONTENT_ON_DEMAND&quot; |



