

# DimensionRange

A range along a single dimension on a sheet. All indexes are zero-based. Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the range is unbounded on that side.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimension** | [**DimensionEnum**](#DimensionEnum) | The dimension of the span. |  [optional] |
|**endIndex** | **Integer** | The end (exclusive) of the span, or not set if unbounded. |  [optional] |
|**sheetId** | **Integer** | The sheet this span is on. |  [optional] |
|**startIndex** | **Integer** | The start (inclusive) of the span, or not set if unbounded. |  [optional] |



## Enum: DimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



