

# NamedStyleSuggestionState

A suggestion state of a NamedStyle message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namedStyleType** | [**NamedStyleTypeEnum**](#NamedStyleTypeEnum) | The named style type that this suggestion state corresponds to. This field is provided as a convenience for matching the NamedStyleSuggestionState with its corresponding NamedStyle. |  [optional] |
|**paragraphStyleSuggestionState** | [**ParagraphStyleSuggestionState**](ParagraphStyleSuggestionState.md) |  |  [optional] |
|**textStyleSuggestionState** | [**TextStyleSuggestionState**](TextStyleSuggestionState.md) |  |  [optional] |



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



