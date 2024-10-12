

# DeleteRangeRequest

Deletes a range of cells, shifting other cells into the deleted area.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**range** | [**GridRange**](GridRange.md) |  |  [optional] |
|**shiftDimension** | [**ShiftDimensionEnum**](#ShiftDimensionEnum) | The dimension from which deleted cells will be replaced with. If ROWS, existing cells will be shifted upward to replace the deleted cells. If COLUMNS, existing cells will be shifted left to replace the deleted cells. |  [optional] |



## Enum: ShiftDimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



