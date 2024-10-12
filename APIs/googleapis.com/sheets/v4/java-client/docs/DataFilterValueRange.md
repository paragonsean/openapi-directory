

# DataFilterValueRange

A range of values whose location is specified by a DataFilter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFilter** | [**DataFilter**](DataFilter.md) |  |  [optional] |
|**majorDimension** | [**MajorDimensionEnum**](#MajorDimensionEnum) | The major dimension of the values. |  [optional] |
|**values** | **List&lt;List&lt;Object&gt;&gt;** | The data to be written. If the provided values exceed any of the ranges matched by the data filter then the request fails. If the provided values are less than the matched ranges only the specified values are written, existing values in the matched ranges remain unaffected. |  [optional] |



## Enum: MajorDimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



