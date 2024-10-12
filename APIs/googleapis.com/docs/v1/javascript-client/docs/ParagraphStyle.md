# GoogleDocsApi.ParagraphStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | **String** | The text alignment for this paragraph. | [optional] 
**avoidWidowAndOrphan** | **Boolean** | Whether to avoid widows and orphans for the paragraph. If unset, the value is inherited from the parent. | [optional] 
**borderBetween** | [**ParagraphBorder**](ParagraphBorder.md) |  | [optional] 
**borderBottom** | [**ParagraphBorder**](ParagraphBorder.md) |  | [optional] 
**borderLeft** | [**ParagraphBorder**](ParagraphBorder.md) |  | [optional] 
**borderRight** | [**ParagraphBorder**](ParagraphBorder.md) |  | [optional] 
**borderTop** | [**ParagraphBorder**](ParagraphBorder.md) |  | [optional] 
**direction** | **String** | The text direction of this paragraph. If unset, the value defaults to LEFT_TO_RIGHT since paragraph direction is not inherited. | [optional] 
**headingId** | **String** | The heading ID of the paragraph. If empty, then this paragraph is not a heading. This property is read-only. | [optional] 
**indentEnd** | [**Dimension**](Dimension.md) |  | [optional] 
**indentFirstLine** | [**Dimension**](Dimension.md) |  | [optional] 
**indentStart** | [**Dimension**](Dimension.md) |  | [optional] 
**keepLinesTogether** | **Boolean** | Whether all lines of the paragraph should be laid out on the same page or column if possible. If unset, the value is inherited from the parent. | [optional] 
**keepWithNext** | **Boolean** | Whether at least a part of this paragraph should be laid out on the same page or column as the next paragraph if possible. If unset, the value is inherited from the parent. | [optional] 
**lineSpacing** | **Number** | The amount of space between lines, as a percentage of normal, where normal is represented as 100.0. If unset, the value is inherited from the parent. | [optional] 
**namedStyleType** | **String** | The named style type of the paragraph. Since updating the named style type affects other properties within ParagraphStyle, the named style type is applied before the other properties are updated. | [optional] 
**pageBreakBefore** | **Boolean** | Whether the current paragraph should always start at the beginning of a page. If unset, the value is inherited from the parent. Attempting to update page_break_before for paragraphs in unsupported regions, including Table, Header, Footer and Footnote, can result in an invalid document state that returns a 400 bad request error. | [optional] 
**shading** | [**Shading**](Shading.md) |  | [optional] 
**spaceAbove** | [**Dimension**](Dimension.md) |  | [optional] 
**spaceBelow** | [**Dimension**](Dimension.md) |  | [optional] 
**spacingMode** | **String** | The spacing mode for the paragraph. | [optional] 
**tabStops** | [**[TabStop]**](TabStop.md) | A list of the tab stops for this paragraph. The list of tab stops is not inherited. This property is read-only. | [optional] 



## Enum: AlignmentEnum


* `ALIGNMENT_UNSPECIFIED` (value: `"ALIGNMENT_UNSPECIFIED"`)

* `START` (value: `"START"`)

* `CENTER` (value: `"CENTER"`)

* `END` (value: `"END"`)

* `JUSTIFIED` (value: `"JUSTIFIED"`)





## Enum: DirectionEnum


* `CONTENT_DIRECTION_UNSPECIFIED` (value: `"CONTENT_DIRECTION_UNSPECIFIED"`)

* `LEFT_TO_RIGHT` (value: `"LEFT_TO_RIGHT"`)

* `RIGHT_TO_LEFT` (value: `"RIGHT_TO_LEFT"`)





## Enum: NamedStyleTypeEnum


* `NAMED_STYLE_TYPE_UNSPECIFIED` (value: `"NAMED_STYLE_TYPE_UNSPECIFIED"`)

* `NORMAL_TEXT` (value: `"NORMAL_TEXT"`)

* `TITLE` (value: `"TITLE"`)

* `SUBTITLE` (value: `"SUBTITLE"`)

* `HEADING_1` (value: `"HEADING_1"`)

* `HEADING_2` (value: `"HEADING_2"`)

* `HEADING_3` (value: `"HEADING_3"`)

* `HEADING_4` (value: `"HEADING_4"`)

* `HEADING_5` (value: `"HEADING_5"`)

* `HEADING_6` (value: `"HEADING_6"`)





## Enum: SpacingModeEnum


* `SPACING_MODE_UNSPECIFIED` (value: `"SPACING_MODE_UNSPECIFIED"`)

* `NEVER_COLLAPSE` (value: `"NEVER_COLLAPSE"`)

* `COLLAPSE_LISTS` (value: `"COLLAPSE_LISTS"`)




