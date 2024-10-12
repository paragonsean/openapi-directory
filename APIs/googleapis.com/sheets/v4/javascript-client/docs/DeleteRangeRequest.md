# GoogleSheetsApi.DeleteRangeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**GridRange**](GridRange.md) |  | [optional] 
**shiftDimension** | **String** | The dimension from which deleted cells will be replaced with. If ROWS, existing cells will be shifted upward to replace the deleted cells. If COLUMNS, existing cells will be shifted left to replace the deleted cells. | [optional] 



## Enum: ShiftDimensionEnum


* `DIMENSION_UNSPECIFIED` (value: `"DIMENSION_UNSPECIFIED"`)

* `ROWS` (value: `"ROWS"`)

* `COLUMNS` (value: `"COLUMNS"`)




