

# NamedStyle

A named style. Paragraphs in the document can inherit their TextStyle and ParagraphStyle from this named style when they have the same named style type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namedStyleType** | [**NamedStyleTypeEnum**](#NamedStyleTypeEnum) | The type of this named style. |  [optional] |
|**paragraphStyle** | [**ParagraphStyle**](ParagraphStyle.md) |  |  [optional] |
|**textStyle** | [**TextStyle**](TextStyle.md) |  |  [optional] |



## Enum: NamedStyleTypeEnum

| Name | Value |
|---- | -----|
| NAMED_STYLE_TYPE_UNSPECIFIED | &quot;NAMED_STYLE_TYPE_UNSPECIFIED&quot; |
| NORMAL_TEXT | &quot;NORMAL_TEXT&quot; |
| TITLE | &quot;TITLE&quot; |
| SUBTITLE | &quot;SUBTITLE&quot; |
| HEADING_1 | &quot;HEADING_1&quot; |
| HEADING_2 | &quot;HEADING_2&quot; |
| HEADING_3 | &quot;HEADING_3&quot; |
| HEADING_4 | &quot;HEADING_4&quot; |
| HEADING_5 | &quot;HEADING_5&quot; |
| HEADING_6 | &quot;HEADING_6&quot; |



