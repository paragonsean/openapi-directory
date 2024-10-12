

# GridData

Data in the grid, as well as metadata about the dimensions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnMetadata** | [**List&lt;DimensionProperties&gt;**](DimensionProperties.md) | Metadata about the requested columns in the grid, starting with the column in start_column. |  [optional] |
|**rowData** | [**List&lt;RowData&gt;**](RowData.md) | The data in the grid, one entry per row, starting with the row in startRow. The values in RowData will correspond to columns starting at start_column. |  [optional] |
|**rowMetadata** | [**List&lt;DimensionProperties&gt;**](DimensionProperties.md) | Metadata about the requested rows in the grid, starting with the row in start_row. |  [optional] |
|**startColumn** | **Integer** | The first column this GridData refers to, zero-based. |  [optional] |
|**startRow** | **Integer** | The first row this GridData refers to, zero-based. |  [optional] |



