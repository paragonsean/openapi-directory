

# VideoPlayerSizeAssignedTargetingOptionDetails

Video player size targeting option details. This will be populated in the video_player_size_details field when targeting_type is `TARGETING_TYPE_VIDEO_PLAYER_SIZE`. Explicitly targeting all options is not supported. Remove all video player size targeting options to achieve this effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetingOptionId** | **String** | Required. The targeting_option_id field when targeting_type is &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60;. |  [optional] |
|**videoPlayerSize** | [**VideoPlayerSizeEnum**](#VideoPlayerSizeEnum) | Required. The video player size. |  [optional] |



## Enum: VideoPlayerSizeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIDEO_PLAYER_SIZE_UNSPECIFIED&quot; |
| SMALL | &quot;VIDEO_PLAYER_SIZE_SMALL&quot; |
| LARGE | &quot;VIDEO_PLAYER_SIZE_LARGE&quot; |
| HD | &quot;VIDEO_PLAYER_SIZE_HD&quot; |
| UNKNOWN | &quot;VIDEO_PLAYER_SIZE_UNKNOWN&quot; |



