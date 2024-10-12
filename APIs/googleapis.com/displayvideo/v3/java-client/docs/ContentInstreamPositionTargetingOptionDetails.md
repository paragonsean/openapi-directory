

# ContentInstreamPositionTargetingOptionDetails

Represents a targetable content instream position, which could be used by video and audio ads. This will be populated in the content_instream_position_details field when targeting_type is `TARGETING_TYPE_CONTENT_INSTREAM_POSITION`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentInstreamPosition** | [**ContentInstreamPositionEnum**](#ContentInstreamPositionEnum) | Output only. The content instream position. |  [optional] [readonly] |



## Enum: ContentInstreamPositionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONTENT_INSTREAM_POSITION_UNSPECIFIED&quot; |
| PRE_ROLL | &quot;CONTENT_INSTREAM_POSITION_PRE_ROLL&quot; |
| MID_ROLL | &quot;CONTENT_INSTREAM_POSITION_MID_ROLL&quot; |
| POST_ROLL | &quot;CONTENT_INSTREAM_POSITION_POST_ROLL&quot; |
| UNKNOWN | &quot;CONTENT_INSTREAM_POSITION_UNKNOWN&quot; |



