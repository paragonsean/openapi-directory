

# SourceAndDestination

A combination of a source range and how to extend that source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | [**DimensionEnum**](#DimensionEnum) | The dimension that data should be filled into. |  [optional] |
|**fillLength** | **Integer** | The number of rows or columns that data should be filled into. Positive numbers expand beyond the last row or last column of the source. Negative numbers expand before the first row or first column of the source. |  [optional] |
|**source** | [**GridRange**](GridRange.md) |  |  [optional] |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



