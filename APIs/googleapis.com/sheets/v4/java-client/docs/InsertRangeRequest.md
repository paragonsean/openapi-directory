

# InsertRangeRequest

Inserts cells into a range, shifting the existing cells over or down.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**range** | [**GridRange**](GridRange.md) |  |  [optional] |
|**shiftDimension** | [**ShiftDimensionEnum**](#ShiftDimensionEnum) | The dimension which will be shifted when inserting cells. If ROWS, existing cells will be shifted down. If COLUMNS, existing cells will be shifted right. |  [optional] |



## Enum: ShiftDimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



