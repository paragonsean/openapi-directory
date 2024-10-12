

# VoiceSelectionParams

Description of which voice to use for a synthesis request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customVoice** | [**CustomVoiceParams**](CustomVoiceParams.md) |  |  [optional] |
|**languageCode** | **String** | Required. The language (and potentially also the region) of the voice expressed as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag, e.g. \&quot;en-US\&quot;. This should not include a script tag (e.g. use \&quot;cmn-cn\&quot; rather than \&quot;cmn-Hant-cn\&quot;), because the script will be inferred from the input provided in the SynthesisInput. The TTS service will use this parameter to help choose an appropriate voice. Note that the TTS service may choose a voice with a slightly different language code than the one selected; it may substitute a different region (e.g. using en-US rather than en-CA if there isn&#39;t a Canadian voice available), or even a different language, e.g. using \&quot;nb\&quot; (Norwegian Bokmal) instead of \&quot;no\&quot; (Norwegian)\&quot;. |  [optional] |
|**name** | **String** | The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and gender. |  [optional] |
|**ssmlGender** | [**SsmlGenderEnum**](#SsmlGenderEnum) | The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as language_code and name. Note that this is only a preference, not requirement; if a voice of the appropriate gender is not available, the synthesizer should substitute a voice with a different gender rather than failing the request. |  [optional] |



## Enum: SsmlGenderEnum

| Name | Value |
|---- | -----|
| SSML_VOICE_GENDER_UNSPECIFIED | &quot;SSML_VOICE_GENDER_UNSPECIFIED&quot; |
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| NEUTRAL | &quot;NEUTRAL&quot; |



