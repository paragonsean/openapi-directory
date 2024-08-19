

# SoundTouchResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| SOUND_TOUCH_EXECUTED | &quot;SoundTouch Executed&quot; |
| CALL_UUID_PARAMETER_MISSING | &quot;CallUUID Parameter Missing&quot; |
| AUDIO_DIRECTION_PARAMETER_MUST_BE_IN_OR_OUT_ | &quot;AudioDirection Parameter Must be &#39;in&#39; or &#39;out&#39;&quot; |
| PITCH_SEMI_TONES_PARAMETER_MUST_BE_FLOAT | &quot;PitchSemiTones Parameter must be float&quot; |
| PITCH_SEMI_TONES_PARAMETER_MUST_BE_BETWEEN_14_AND_14 | &quot;PitchSemiTones Parameter must be between -14 and 14&quot; |
| PITCH_OCTAVES_PARAMETER_MUST_BE_FLOAT | &quot;PitchOctaves Parameter must be float&quot; |
| PITCH_OCTAVES_PARAMETER_MUST_BE_BETWEEN_1_AND_1 | &quot;PitchOctaves Parameter must be between -1 and 1&quot; |
| PITCH_PARAMETER_MUST_BE_FLOAT | &quot;Pitch Parameter must be float&quot; |
| PITCH_PARAMETER_MUST_BE_0 | &quot;Pitch Parameter must be &gt; 0&quot; |
| RATE_PARAMETER_MUST_BE_FLOAT | &quot;Rate Parameter must be float&quot; |
| RATE_PARAMETER_MUST_BE_0 | &quot;Rate Parameter must be &gt; 0&quot; |
| TEMPO_PARAMETER_MUST_BE_FLOAT | &quot;Tempo Parameter must be float&quot; |
| TEMPO_PARAMETER_MUST_BE_0 | &quot;Tempo Parameter must be &gt; 0&quot; |
| SOUND_TOUCH_FAILED_CALL_NOT_FOUND | &quot;SoundTouch Failed -- Call not found&quot; |
| SOUND_TOUCH_FAILED | &quot;SoundTouch Failed&quot; |



