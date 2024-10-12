

# TextStyle

Represents the styling that can be applied to a TextRun. If this text is contained in a shape with a parent placeholder, then these text styles may be inherited from the parent. Which text styles are inherited depend on the nesting level of lists: * A text run in a paragraph that is not in a list will inherit its text style from the the newline character in the paragraph at the 0 nesting level of the list inside the parent placeholder. * A text run in a paragraph that is in a list will inherit its text style from the newline character in the paragraph at its corresponding nesting level of the list inside the parent placeholder. Inherited text styles are represented as unset fields in this message. If text is contained in a shape without a parent placeholder, unsetting these fields will revert the style to a value matching the defaults in the Slides editor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundColor** | [**OptionalColor**](OptionalColor.md) |  |  [optional] |
|**baselineOffset** | [**BaselineOffsetEnum**](#BaselineOffsetEnum) | The text&#39;s vertical offset from its normal position. Text with &#x60;SUPERSCRIPT&#x60; or &#x60;SUBSCRIPT&#x60; baseline offsets is automatically rendered in a smaller font size, computed based on the &#x60;font_size&#x60; field. The &#x60;font_size&#x60; itself is not affected by changes in this field. |  [optional] |
|**bold** | **Boolean** | Whether or not the text is rendered as bold. |  [optional] |
|**fontFamily** | **String** | The font family of the text. The font family can be any font from the Font menu in Slides or from [Google Fonts] (https://fonts.google.com/). If the font name is unrecognized, the text is rendered in &#x60;Arial&#x60;. Some fonts can affect the weight of the text. If an update request specifies values for both &#x60;font_family&#x60; and &#x60;bold&#x60;, the explicitly-set &#x60;bold&#x60; value is used. |  [optional] |
|**fontSize** | [**Dimension**](Dimension.md) |  |  [optional] |
|**foregroundColor** | [**OptionalColor**](OptionalColor.md) |  |  [optional] |
|**italic** | **Boolean** | Whether or not the text is italicized. |  [optional] |
|**link** | [**Link**](Link.md) |  |  [optional] |
|**smallCaps** | **Boolean** | Whether or not the text is in small capital letters. |  [optional] |
|**strikethrough** | **Boolean** | Whether or not the text is struck through. |  [optional] |
|**underline** | **Boolean** | Whether or not the text is underlined. |  [optional] |
|**weightedFontFamily** | [**WeightedFontFamily**](WeightedFontFamily.md) |  |  [optional] |



## Enum: BaselineOffsetEnum

| Name | Value |
|---- | -----|
| BASELINE_OFFSET_UNSPECIFIED | &quot;BASELINE_OFFSET_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| SUPERSCRIPT | &quot;SUPERSCRIPT&quot; |
| SUBSCRIPT | &quot;SUBSCRIPT&quot; |



