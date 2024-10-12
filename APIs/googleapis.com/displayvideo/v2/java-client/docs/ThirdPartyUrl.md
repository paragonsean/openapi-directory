

# ThirdPartyUrl

Tracking URLs from third parties to track interactions with an audio or a video creative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of interaction needs to be tracked by the tracking URL |  [optional] |
|**url** | **String** | Tracking URL used to track the interaction. Provide a URL with optional path or query string, beginning with &#x60;https:&#x60;. For example, https://www.example.com/path |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;THIRD_PARTY_URL_TYPE_UNSPECIFIED&quot; |
| IMPRESSION | &quot;THIRD_PARTY_URL_TYPE_IMPRESSION&quot; |
| CLICK_TRACKING | &quot;THIRD_PARTY_URL_TYPE_CLICK_TRACKING&quot; |
| AUDIO_VIDEO_START | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_START&quot; |
| AUDIO_VIDEO_FIRST_QUARTILE | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_FIRST_QUARTILE&quot; |
| AUDIO_VIDEO_MIDPOINT | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_MIDPOINT&quot; |
| AUDIO_VIDEO_THIRD_QUARTILE | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_THIRD_QUARTILE&quot; |
| AUDIO_VIDEO_COMPLETE | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_COMPLETE&quot; |
| AUDIO_VIDEO_MUTE | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_MUTE&quot; |
| AUDIO_VIDEO_PAUSE | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_PAUSE&quot; |
| AUDIO_VIDEO_REWIND | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_REWIND&quot; |
| AUDIO_VIDEO_FULLSCREEN | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_FULLSCREEN&quot; |
| AUDIO_VIDEO_STOP | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_STOP&quot; |
| AUDIO_VIDEO_CUSTOM | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_CUSTOM&quot; |
| AUDIO_VIDEO_SKIP | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_SKIP&quot; |
| AUDIO_VIDEO_PROGRESS | &quot;THIRD_PARTY_URL_TYPE_AUDIO_VIDEO_PROGRESS&quot; |



