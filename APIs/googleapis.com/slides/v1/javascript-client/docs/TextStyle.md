# GoogleSlidesApi.TextStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backgroundColor** | [**OptionalColor**](OptionalColor.md) |  | [optional] 
**baselineOffset** | **String** | The text&#39;s vertical offset from its normal position. Text with &#x60;SUPERSCRIPT&#x60; or &#x60;SUBSCRIPT&#x60; baseline offsets is automatically rendered in a smaller font size, computed based on the &#x60;font_size&#x60; field. The &#x60;font_size&#x60; itself is not affected by changes in this field. | [optional] 
**bold** | **Boolean** | Whether or not the text is rendered as bold. | [optional] 
**fontFamily** | **String** | The font family of the text. The font family can be any font from the Font menu in Slides or from [Google Fonts] (https://fonts.google.com/). If the font name is unrecognized, the text is rendered in &#x60;Arial&#x60;. Some fonts can affect the weight of the text. If an update request specifies values for both &#x60;font_family&#x60; and &#x60;bold&#x60;, the explicitly-set &#x60;bold&#x60; value is used. | [optional] 
**fontSize** | [**Dimension**](Dimension.md) |  | [optional] 
**foregroundColor** | [**OptionalColor**](OptionalColor.md) |  | [optional] 
**italic** | **Boolean** | Whether or not the text is italicized. | [optional] 
**link** | [**Link**](Link.md) |  | [optional] 
**smallCaps** | **Boolean** | Whether or not the text is in small capital letters. | [optional] 
**strikethrough** | **Boolean** | Whether or not the text is struck through. | [optional] 
**underline** | **Boolean** | Whether or not the text is underlined. | [optional] 
**weightedFontFamily** | [**WeightedFontFamily**](WeightedFontFamily.md) |  | [optional] 



## Enum: BaselineOffsetEnum


* `BASELINE_OFFSET_UNSPECIFIED` (value: `"BASELINE_OFFSET_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `SUPERSCRIPT` (value: `"SUPERSCRIPT"`)

* `SUBSCRIPT` (value: `"SUBSCRIPT"`)




