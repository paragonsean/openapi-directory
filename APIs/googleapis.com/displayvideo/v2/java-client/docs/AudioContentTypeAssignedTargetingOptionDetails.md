

# AudioContentTypeAssignedTargetingOptionDetails

Details for audio content type assigned targeting option. This will be populated in the audio_content_type_details field when targeting_type is `TARGETING_TYPE_AUDIO_CONTENT_TYPE`. Explicitly targeting all options is not supported. Remove all audio content type targeting options to achieve this effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioContentType** | [**AudioContentTypeEnum**](#AudioContentTypeEnum) | Required. The audio content type. |  [optional] |



## Enum: AudioContentTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUDIO_CONTENT_TYPE_UNSPECIFIED&quot; |
| UNKNOWN | &quot;AUDIO_CONTENT_TYPE_UNKNOWN&quot; |
| MUSIC | &quot;AUDIO_CONTENT_TYPE_MUSIC&quot; |
| BROADCAST | &quot;AUDIO_CONTENT_TYPE_BROADCAST&quot; |
| PODCAST | &quot;AUDIO_CONTENT_TYPE_PODCAST&quot; |



