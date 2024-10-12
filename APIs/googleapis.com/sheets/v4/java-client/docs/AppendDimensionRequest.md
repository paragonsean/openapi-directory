

# AppendDimensionRequest

Appends rows or columns to the end of a sheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | [**DimensionEnum**](#DimensionEnum) | Whether rows or columns should be appended. |  [optional] |
|**length** | **Integer** | The number of rows or columns to append. |  [optional] |
|**sheetId** | **Integer** | The sheet to append rows or columns to. |  [optional] |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



