# DialogflowApi.GoogleCloudDialogflowV2VoiceSelectionParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and ssml_gender. | [optional] 
**ssmlGender** | **String** | Optional. The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and name. Note that this is only a preference, not requirement. If a voice of the appropriate gender is not available, the synthesizer should substitute a voice with a different gender rather than failing the request. | [optional] 



## Enum: SsmlGenderEnum


* `UNSPECIFIED` (value: `"SSML_VOICE_GENDER_UNSPECIFIED"`)

* `MALE` (value: `"SSML_VOICE_GENDER_MALE"`)

* `FEMALE` (value: `"SSML_VOICE_GENDER_FEMALE"`)

* `NEUTRAL` (value: `"SSML_VOICE_GENDER_NEUTRAL"`)




