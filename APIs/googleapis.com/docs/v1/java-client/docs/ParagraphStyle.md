

# ParagraphStyle

Styles that apply to a whole paragraph. Inherited paragraph styles are represented as unset fields in this message. A paragraph style's parent depends on where the paragraph style is defined: * The ParagraphStyle on a Paragraph inherits from the paragraph's corresponding named style type. * The ParagraphStyle on a named style inherits from the normal text named style. * The ParagraphStyle of the normal text named style inherits from the default paragraph style in the Docs editor. * The ParagraphStyle on a Paragraph element that's contained in a table may inherit its paragraph style from the table style. If the paragraph style does not inherit from a parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alignment** | [**AlignmentEnum**](#AlignmentEnum) | The text alignment for this paragraph. |  [optional] |
|**avoidWidowAndOrphan** | **Boolean** | Whether to avoid widows and orphans for the paragraph. If unset, the value is inherited from the parent. |  [optional] |
|**borderBetween** | [**ParagraphBorder**](ParagraphBorder.md) |  |  [optional] |
|**borderBottom** | [**ParagraphBorder**](ParagraphBorder.md) |  |  [optional] |
|**borderLeft** | [**ParagraphBorder**](ParagraphBorder.md) |  |  [optional] |
|**borderRight** | [**ParagraphBorder**](ParagraphBorder.md) |  |  [optional] |
|**borderTop** | [**ParagraphBorder**](ParagraphBorder.md) |  |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The text direction of this paragraph. If unset, the value defaults to LEFT_TO_RIGHT since paragraph direction is not inherited. |  [optional] |
|**headingId** | **String** | The heading ID of the paragraph. If empty, then this paragraph is not a heading. This property is read-only. |  [optional] |
|**indentEnd** | [**Dimension**](Dimension.md) |  |  [optional] |
|**indentFirstLine** | [**Dimension**](Dimension.md) |  |  [optional] |
|**indentStart** | [**Dimension**](Dimension.md) |  |  [optional] |
|**keepLinesTogether** | **Boolean** | Whether all lines of the paragraph should be laid out on the same page or column if possible. If unset, the value is inherited from the parent. |  [optional] |
|**keepWithNext** | **Boolean** | Whether at least a part of this paragraph should be laid out on the same page or column as the next paragraph if possible. If unset, the value is inherited from the parent. |  [optional] |
|**lineSpacing** | **Float** | The amount of space between lines, as a percentage of normal, where normal is represented as 100.0. If unset, the value is inherited from the parent. |  [optional] |
|**namedStyleType** | [**NamedStyleTypeEnum**](#NamedStyleTypeEnum) | The named style type of the paragraph. Since updating the named style type affects other properties within ParagraphStyle, the named style type is applied before the other properties are updated. |  [optional] |
|**pageBreakBefore** | **Boolean** | Whether the current paragraph should always start at the beginning of a page. If unset, the value is inherited from the parent. Attempting to update page_break_before for paragraphs in unsupported regions, including Table, Header, Footer and Footnote, can result in an invalid document state that returns a 400 bad request error. |  [optional] |
|**shading** | [**Shading**](Shading.md) |  |  [optional] |
|**spaceAbove** | [**Dimension**](Dimension.md) |  |  [optional] |
|**spaceBelow** | [**Dimension**](Dimension.md) |  |  [optional] |
|**spacingMode** | [**SpacingModeEnum**](#SpacingModeEnum) | The spacing mode for the paragraph. |  [optional] |
|**tabStops** | [**List&lt;TabStop&gt;**](TabStop.md) | A list of the tab stops for this paragraph. The list of tab stops is not inherited. This property is read-only. |  [optional] |



## Enum: AlignmentEnum

| Name | Value |
|---- | -----|
| ALIGNMENT_UNSPECIFIED | &quot;ALIGNMENT_UNSPECIFIED&quot; |
| START | &quot;START&quot; |
| CENTER | &quot;CENTER&quot; |
| END | &quot;END&quot; |
| JUSTIFIED | &quot;JUSTIFIED&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| CONTENT_DIRECTION_UNSPECIFIED | &quot;CONTENT_DIRECTION_UNSPECIFIED&quot; |
| LEFT_TO_RIGHT | &quot;LEFT_TO_RIGHT&quot; |
| RIGHT_TO_LEFT | &quot;RIGHT_TO_LEFT&quot; |



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



## Enum: SpacingModeEnum

| Name | Value |
|---- | -----|
| SPACING_MODE_UNSPECIFIED | &quot;SPACING_MODE_UNSPECIFIED&quot; |
| NEVER_COLLAPSE | &quot;NEVER_COLLAPSE&quot; |
| COLLAPSE_LISTS | &quot;COLLAPSE_LISTS&quot; |



