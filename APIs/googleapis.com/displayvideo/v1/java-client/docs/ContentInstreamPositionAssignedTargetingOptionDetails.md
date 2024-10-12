

# ContentInstreamPositionAssignedTargetingOptionDetails

Assigned content instream position targeting option details. This will be populated in the content_instream_position_details field when targeting_type is `TARGETING_TYPE_CONTENT_INSTREAM_POSITION`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adType** | [**AdTypeEnum**](#AdTypeEnum) | Output only. The ad type to target. Only applicable to insertion order targeting and new line items supporting the specified ad type will inherit this targeting option by default. Possible values are: * &#x60;AD_TYPE_VIDEO&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_VIDEO_DEFAULT&#x60;. * &#x60;AD_TYPE_AUDIO&#x60;, the setting will be inherited by new line item when line_item_type is &#x60;LINE_ITEM_TYPE_AUDIO_DEFAULT&#x60;. |  [optional] [readonly] |
|**contentInstreamPosition** | [**ContentInstreamPositionEnum**](#ContentInstreamPositionEnum) | Required. The content instream position for video or audio ads. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60;. |  [optional] |



## Enum: AdTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AD_TYPE_UNSPECIFIED&quot; |
| DISPLAY | &quot;AD_TYPE_DISPLAY&quot; |
| VIDEO | &quot;AD_TYPE_VIDEO&quot; |
| AUDIO | &quot;AD_TYPE_AUDIO&quot; |



## Enum: ContentInstreamPositionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONTENT_INSTREAM_POSITION_UNSPECIFIED&quot; |
| PRE_ROLL | &quot;CONTENT_INSTREAM_POSITION_PRE_ROLL&quot; |
| MID_ROLL | &quot;CONTENT_INSTREAM_POSITION_MID_ROLL&quot; |
| POST_ROLL | &quot;CONTENT_INSTREAM_POSITION_POST_ROLL&quot; |
| UNKNOWN | &quot;CONTENT_INSTREAM_POSITION_UNKNOWN&quot; |



