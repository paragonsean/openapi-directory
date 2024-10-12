

# CellFormat

The format of a cell.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundColor** | [**Color**](Color.md) |  |  [optional] |
|**backgroundColorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**borders** | [**Borders**](Borders.md) |  |  [optional] |
|**horizontalAlignment** | [**HorizontalAlignmentEnum**](#HorizontalAlignmentEnum) | The horizontal alignment of the value in the cell. |  [optional] |
|**hyperlinkDisplayType** | [**HyperlinkDisplayTypeEnum**](#HyperlinkDisplayTypeEnum) | If one exists, how a hyperlink should be displayed in the cell. |  [optional] |
|**numberFormat** | [**NumberFormat**](NumberFormat.md) |  |  [optional] |
|**padding** | [**Padding**](Padding.md) |  |  [optional] |
|**textDirection** | [**TextDirectionEnum**](#TextDirectionEnum) | The direction of the text in the cell. |  [optional] |
|**textFormat** | [**TextFormat**](TextFormat.md) |  |  [optional] |
|**textRotation** | [**TextRotation**](TextRotation.md) |  |  [optional] |
|**verticalAlignment** | [**VerticalAlignmentEnum**](#VerticalAlignmentEnum) | The vertical alignment of the value in the cell. |  [optional] |
|**wrapStrategy** | [**WrapStrategyEnum**](#WrapStrategyEnum) | The wrap strategy for the value in the cell. |  [optional] |



## Enum: HorizontalAlignmentEnum

| Name | Value |
|---- | -----|
| HORIZONTAL_ALIGN_UNSPECIFIED | &quot;HORIZONTAL_ALIGN_UNSPECIFIED&quot; |
| LEFT | &quot;LEFT&quot; |
| CENTER | &quot;CENTER&quot; |
| RIGHT | &quot;RIGHT&quot; |



## Enum: HyperlinkDisplayTypeEnum

| Name | Value |
|---- | -----|
| HYPERLINK_DISPLAY_TYPE_UNSPECIFIED | &quot;HYPERLINK_DISPLAY_TYPE_UNSPECIFIED&quot; |
| LINKED | &quot;LINKED&quot; |
| PLAIN_TEXT | &quot;PLAIN_TEXT&quot; |



## Enum: TextDirectionEnum

| Name | Value |
|---- | -----|
| TEXT_DIRECTION_UNSPECIFIED | &quot;TEXT_DIRECTION_UNSPECIFIED&quot; |
| LEFT_TO_RIGHT | &quot;LEFT_TO_RIGHT&quot; |
| RIGHT_TO_LEFT | &quot;RIGHT_TO_LEFT&quot; |



## Enum: VerticalAlignmentEnum

| Name | Value |
|---- | -----|
| VERTICAL_ALIGN_UNSPECIFIED | &quot;VERTICAL_ALIGN_UNSPECIFIED&quot; |
| TOP | &quot;TOP&quot; |
| MIDDLE | &quot;MIDDLE&quot; |
| BOTTOM | &quot;BOTTOM&quot; |



## Enum: WrapStrategyEnum

| Name | Value |
|---- | -----|
| WRAP_STRATEGY_UNSPECIFIED | &quot;WRAP_STRATEGY_UNSPECIFIED&quot; |
| OVERFLOW_CELL | &quot;OVERFLOW_CELL&quot; |
| LEGACY_WRAP | &quot;LEGACY_WRAP&quot; |
| CLIP | &quot;CLIP&quot; |
| WRAP | &quot;WRAP&quot; |



