# GoogleSlidesApi.ParagraphStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignment** | **String** | The text alignment for this paragraph. | [optional] 
**direction** | **String** | The text direction of this paragraph. If unset, the value defaults to LEFT_TO_RIGHT since text direction is not inherited. | [optional] 
**indentEnd** | [**Dimension**](Dimension.md) |  | [optional] 
**indentFirstLine** | [**Dimension**](Dimension.md) |  | [optional] 
**indentStart** | [**Dimension**](Dimension.md) |  | [optional] 
**lineSpacing** | **Number** | The amount of space between lines, as a percentage of normal, where normal is represented as 100.0. If unset, the value is inherited from the parent. | [optional] 
**spaceAbove** | [**Dimension**](Dimension.md) |  | [optional] 
**spaceBelow** | [**Dimension**](Dimension.md) |  | [optional] 
**spacingMode** | **String** | The spacing mode for the paragraph. | [optional] 



## Enum: AlignmentEnum


* `ALIGNMENT_UNSPECIFIED` (value: `"ALIGNMENT_UNSPECIFIED"`)

* `START` (value: `"START"`)

* `CENTER` (value: `"CENTER"`)

* `END` (value: `"END"`)

* `JUSTIFIED` (value: `"JUSTIFIED"`)





## Enum: DirectionEnum


* `TEXT_DIRECTION_UNSPECIFIED` (value: `"TEXT_DIRECTION_UNSPECIFIED"`)

* `LEFT_TO_RIGHT` (value: `"LEFT_TO_RIGHT"`)

* `RIGHT_TO_LEFT` (value: `"RIGHT_TO_LEFT"`)





## Enum: SpacingModeEnum


* `SPACING_MODE_UNSPECIFIED` (value: `"SPACING_MODE_UNSPECIFIED"`)

* `NEVER_COLLAPSE` (value: `"NEVER_COLLAPSE"`)

* `COLLAPSE_LISTS` (value: `"COLLAPSE_LISTS"`)




