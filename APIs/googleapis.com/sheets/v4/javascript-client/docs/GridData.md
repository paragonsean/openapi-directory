# GoogleSheetsApi.GridData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnMetadata** | [**[DimensionProperties]**](DimensionProperties.md) | Metadata about the requested columns in the grid, starting with the column in start_column. | [optional] 
**rowData** | [**[RowData]**](RowData.md) | The data in the grid, one entry per row, starting with the row in startRow. The values in RowData will correspond to columns starting at start_column. | [optional] 
**rowMetadata** | [**[DimensionProperties]**](DimensionProperties.md) | Metadata about the requested rows in the grid, starting with the row in start_row. | [optional] 
**startColumn** | **Number** | The first column this GridData refers to, zero-based. | [optional] 
**startRow** | **Number** | The first row this GridData refers to, zero-based. | [optional] 


