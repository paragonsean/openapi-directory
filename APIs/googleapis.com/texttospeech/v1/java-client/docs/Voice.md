

# Voice

Description of a voice supported by the TTS service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCodes** | **List&lt;String&gt;** | The languages that this voice supports, expressed as [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tags (e.g. \&quot;en-US\&quot;, \&quot;es-419\&quot;, \&quot;cmn-tw\&quot;). |  [optional] |
|**name** | **String** | The name of this voice. Each distinct voice has a unique name. |  [optional] |
|**naturalSampleRateHertz** | **Integer** | The natural sample rate (in hertz) for this voice. |  [optional] |
|**ssmlGender** | [**SsmlGenderEnum**](#SsmlGenderEnum) | The gender of this voice. |  [optional] |



## Enum: SsmlGenderEnum

| Name | Value |
|---- | -----|
| SSML_VOICE_GENDER_UNSPECIFIED | &quot;SSML_VOICE_GENDER_UNSPECIFIED&quot; |
| MALE | &quot;MALE&quot; |
| FEMALE | &quot;FEMALE&quot; |
| NEUTRAL | &quot;NEUTRAL&quot; |



