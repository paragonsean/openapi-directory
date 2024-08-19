# TranscoderApi.TextStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **String** | The codec for this text stream. The default is &#x60;webvtt&#x60;. Supported text codecs: - &#x60;srt&#x60; - &#x60;ttml&#x60; - &#x60;cea608&#x60; - &#x60;cea708&#x60; - &#x60;webvtt&#x60; | [optional] 
**displayName** | **String** | The name for this particular text stream that will be added to the HLS/DASH manifest. Not supported in MP4 files. | [optional] 
**languageCode** | **String** | The BCP-47 language code, such as &#x60;en-US&#x60; or &#x60;sr-Latn&#x60;. For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. Not supported in MP4 files. | [optional] 
**mapping** | [**[TextMapping]**](TextMapping.md) | The mapping for the JobConfig.edit_list atoms with text EditAtom.inputs. | [optional] 


