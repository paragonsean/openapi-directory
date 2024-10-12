

# Dimension

A chart dimension. Dimensions are a structured label, class, or category for a set of measurements in your data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | Required. The name of the column in the source SQL query that is used to chart the dimension. |  [optional] |
|**columnType** | **String** | Optional. The type of the dimension column. This is relevant only if one of the bin_size fields is set. If it is empty, the type TIMESTAMP or INT64 will be assumed based on which bin_size field is set. If populated, this should be set to one of the following types: DATE, TIME, DATETIME, TIMESTAMP, BIGNUMERIC, INT64, NUMERIC, FLOAT64. |  [optional] |
|**floatBinSize** | **Double** | Optional. float_bin_size is used when the column type used for a dimension is a floating point numeric column. |  [optional] |
|**maxBinCount** | **Integer** | A limit to the number of bins generated. When 0 is specified, the maximum count is not enforced. |  [optional] |
|**numericBinSize** | **Integer** | numeric_bin_size is used when the column type used for a dimension is numeric or string. |  [optional] |
|**sortColumn** | **String** | The column name to sort on for binning. This column can be the same column as this dimension or any other column used as a measure in the results. If sort_order is set to NONE, then this value is not used. |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) | The sort order applied to the sort column. |  [optional] |
|**timeBinSize** | **String** | time_bin_size is used when the data type specified by column is a time type and the bin size is determined by a time duration. If column_type is DATE, this must be a whole value multiple of 1 day. If column_type is TIME, this must be less than or equal to 24 hours. |  [optional] |



## Enum: SortOrderEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SORT_ORDER_UNSPECIFIED&quot; |
| NONE | &quot;SORT_ORDER_NONE&quot; |
| ASCENDING | &quot;SORT_ORDER_ASCENDING&quot; |
| DESCENDING | &quot;SORT_ORDER_DESCENDING&quot; |



