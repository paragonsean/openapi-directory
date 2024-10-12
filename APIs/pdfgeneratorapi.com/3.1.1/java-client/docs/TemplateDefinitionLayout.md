

# TemplateDefinitionLayout

Defines template layout (e.g page format, margins).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emptyLabels** | **Integer** | Defines how many pages or labels should be empty |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Defines template page size |  [optional] |
|**height** | **BigDecimal** | Page height in units |  [optional] |
|**margins** | [**TemplateDefinitionLayoutMargins**](TemplateDefinitionLayoutMargins.md) |  |  [optional] |
|**orientation** | [**OrientationEnum**](#OrientationEnum) | Page orientation |  [optional] |
|**repeatLayout** | [**TemplateDefinitionLayoutRepeatLayout**](TemplateDefinitionLayoutRepeatLayout.md) |  |  [optional] |
|**rotation** | [**RotationEnum**](#RotationEnum) | Page rotation in degrees |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | Measure unit |  [optional] |
|**width** | **BigDecimal** | Page width in units |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| A4 | &quot;A4&quot; |
| LETTER | &quot;letter&quot; |
| CUSTOM | &quot;custom&quot; |



## Enum: OrientationEnum

| Name | Value |
|---- | -----|
| PORTRAIT | &quot;portrait&quot; |
| LANDSCAPE | &quot;landscape&quot; |



## Enum: RotationEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_90 | 90 |
| NUMBER_180 | 180 |
| NUMBER_270 | 270 |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| CM | &quot;cm&quot; |
| IN | &quot;in&quot; |



