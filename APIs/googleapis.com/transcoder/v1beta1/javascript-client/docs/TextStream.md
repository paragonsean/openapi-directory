# TranscoderApi.TextStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codec** | **String** | The codec for this text stream. The default is &#x60;\&quot;webvtt\&quot;&#x60;. Supported text codecs: - &#39;srt&#39; - &#39;ttml&#39; - &#39;cea608&#39; - &#39;cea708&#39; - &#39;webvtt&#39; | [optional] 
**languageCode** | **String** | Required. The BCP-47 language code, such as &#x60;\&quot;en-US\&quot;&#x60; or &#x60;\&quot;sr-Latn\&quot;&#x60;. For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. | [optional] 
**mapping** | [**[TextAtom]**](TextAtom.md) | The mapping for the &#x60;Job.edit_list&#x60; atoms with text &#x60;EditAtom.inputs&#x60;. | [optional] 


