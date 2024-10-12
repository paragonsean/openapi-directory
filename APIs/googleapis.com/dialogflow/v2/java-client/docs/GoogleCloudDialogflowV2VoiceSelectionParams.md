

# GoogleCloudDialogflowV2VoiceSelectionParams

Description of which voice to use for speech synthesis.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and ssml_gender. |  [optional] |
|**ssmlGender** | [**SsmlGenderEnum**](#SsmlGenderEnum) | Optional. The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and name. Note that this is only a preference, not requirement. If a voice of the appropriate gender is not available, the synthesizer should substitute a voice with a different gender rather than failing the request. |  [optional] |



## Enum: SsmlGenderEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SSML_VOICE_GENDER_UNSPECIFIED&quot; |
| MALE | &quot;SSML_VOICE_GENDER_MALE&quot; |
| FEMALE | &quot;SSML_VOICE_GENDER_FEMALE&quot; |
| NEUTRAL | &quot;SSML_VOICE_GENDER_NEUTRAL&quot; |



