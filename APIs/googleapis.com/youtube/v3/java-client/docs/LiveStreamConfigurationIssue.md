

# LiveStreamConfigurationIssue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The long-form description of the issue and how to resolve it. |  [optional] |
|**reason** | **String** | The short-form reason for this issue. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | How severe this issue is to the stream. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The kind of error happening. |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFO | &quot;info&quot; |
| WARNING | &quot;warning&quot; |
| ERROR | &quot;error&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GOP_SIZE_OVER | &quot;gopSizeOver&quot; |
| GOP_SIZE_LONG | &quot;gopSizeLong&quot; |
| GOP_SIZE_SHORT | &quot;gopSizeShort&quot; |
| OPEN_GOP | &quot;openGop&quot; |
| BAD_CONTAINER | &quot;badContainer&quot; |
| AUDIO_BITRATE_HIGH | &quot;audioBitrateHigh&quot; |
| AUDIO_BITRATE_LOW | &quot;audioBitrateLow&quot; |
| AUDIO_SAMPLE_RATE | &quot;audioSampleRate&quot; |
| BITRATE_HIGH | &quot;bitrateHigh&quot; |
| BITRATE_LOW | &quot;bitrateLow&quot; |
| AUDIO_CODEC | &quot;audioCodec&quot; |
| VIDEO_CODEC | &quot;videoCodec&quot; |
| NO_AUDIO_STREAM | &quot;noAudioStream&quot; |
| NO_VIDEO_STREAM | &quot;noVideoStream&quot; |
| MULTIPLE_VIDEO_STREAMS | &quot;multipleVideoStreams&quot; |
| MULTIPLE_AUDIO_STREAMS | &quot;multipleAudioStreams&quot; |
| AUDIO_TOO_MANY_CHANNELS | &quot;audioTooManyChannels&quot; |
| INTERLACED_VIDEO | &quot;interlacedVideo&quot; |
| FRAME_RATE_HIGH | &quot;frameRateHigh&quot; |
| RESOLUTION_MISMATCH | &quot;resolutionMismatch&quot; |
| VIDEO_CODEC_MISMATCH | &quot;videoCodecMismatch&quot; |
| VIDEO_INTERLACE_MISMATCH | &quot;videoInterlaceMismatch&quot; |
| VIDEO_PROFILE_MISMATCH | &quot;videoProfileMismatch&quot; |
| VIDEO_BITRATE_MISMATCH | &quot;videoBitrateMismatch&quot; |
| FRAMERATE_MISMATCH | &quot;framerateMismatch&quot; |
| GOP_MISMATCH | &quot;gopMismatch&quot; |
| AUDIO_SAMPLE_RATE_MISMATCH | &quot;audioSampleRateMismatch&quot; |
| AUDIO_STEREO_MISMATCH | &quot;audioStereoMismatch&quot; |
| AUDIO_CODEC_MISMATCH | &quot;audioCodecMismatch&quot; |
| AUDIO_BITRATE_MISMATCH | &quot;audioBitrateMismatch&quot; |
| VIDEO_RESOLUTION_SUBOPTIMAL | &quot;videoResolutionSuboptimal&quot; |
| VIDEO_RESOLUTION_UNSUPPORTED | &quot;videoResolutionUnsupported&quot; |
| VIDEO_INGESTION_STARVED | &quot;videoIngestionStarved&quot; |
| VIDEO_INGESTION_FASTER_THAN_REALTIME | &quot;videoIngestionFasterThanRealtime&quot; |



