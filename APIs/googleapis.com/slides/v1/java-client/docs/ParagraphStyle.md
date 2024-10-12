

# ParagraphStyle

Styles that apply to a whole paragraph. If this text is contained in a shape with a parent placeholder, then these paragraph styles may be inherited from the parent. Which paragraph styles are inherited depend on the nesting level of lists: * A paragraph not in a list will inherit its paragraph style from the paragraph at the 0 nesting level of the list inside the parent placeholder. * A paragraph in a list will inherit its paragraph style from the paragraph at its corresponding nesting level of the list inside the parent placeholder. Inherited paragraph styles are represented as unset fields in this message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alignment** | [**AlignmentEnum**](#AlignmentEnum) | The text alignment for this paragraph. |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | The text direction of this paragraph. If unset, the value defaults to LEFT_TO_RIGHT since text direction is not inherited. |  [optional] |
|**indentEnd** | [**Dimension**](Dimension.md) |  |  [optional] |
|**indentFirstLine** | [**Dimension**](Dimension.md) |  |  [optional] |
|**indentStart** | [**Dimension**](Dimension.md) |  |  [optional] |
|**lineSpacing** | **Float** | The amount of space between lines, as a percentage of normal, where normal is represented as 100.0. If unset, the value is inherited from the parent. |  [optional] |
|**spaceAbove** | [**Dimension**](Dimension.md) |  |  [optional] |
|**spaceBelow** | [**Dimension**](Dimension.md) |  |  [optional] |
|**spacingMode** | [**SpacingModeEnum**](#SpacingModeEnum) | The spacing mode for the paragraph. |  [optional] |



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
| TEXT_DIRECTION_UNSPECIFIED | &quot;TEXT_DIRECTION_UNSPECIFIED&quot; |
| LEFT_TO_RIGHT | &quot;LEFT_TO_RIGHT&quot; |
| RIGHT_TO_LEFT | &quot;RIGHT_TO_LEFT&quot; |



## Enum: SpacingModeEnum

| Name | Value |
|---- | -----|
| SPACING_MODE_UNSPECIFIED | &quot;SPACING_MODE_UNSPECIFIED&quot; |
| NEVER_COLLAPSE | &quot;NEVER_COLLAPSE&quot; |
| COLLAPSE_LISTS | &quot;COLLAPSE_LISTS&quot; |



