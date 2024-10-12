# GoogleSheetsApi.UpdateCellsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **String** | The fields of CellData that should be updated. At least one field must be specified. The root is the CellData; &#39;row.values.&#39; should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. | [optional] 
**range** | [**GridRange**](GridRange.md) |  | [optional] 
**rows** | [**[RowData]**](RowData.md) | The data to write. | [optional] 
**start** | [**GridCoordinate**](GridCoordinate.md) |  | [optional] 


