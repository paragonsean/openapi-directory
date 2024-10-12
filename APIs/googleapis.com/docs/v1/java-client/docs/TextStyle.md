

# TextStyle

Represents the styling that can be applied to text. Inherited text styles are represented as unset fields in this message. A text style's parent depends on where the text style is defined: * The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's contained in a table may inherit its text style from the table style. If the text style does not inherit from a parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundColor** | [**OptionalColor**](OptionalColor.md) |  |  [optional] |
|**baselineOffset** | [**BaselineOffsetEnum**](#BaselineOffsetEnum) | The text&#39;s vertical offset from its normal position. Text with &#x60;SUPERSCRIPT&#x60; or &#x60;SUBSCRIPT&#x60; baseline offsets is automatically rendered in a smaller font size, computed based on the &#x60;font_size&#x60; field. Changes in this field don&#39;t affect the &#x60;font_size&#x60;. |  [optional] |
|**bold** | **Boolean** | Whether or not the text is rendered as bold. |  [optional] |
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



