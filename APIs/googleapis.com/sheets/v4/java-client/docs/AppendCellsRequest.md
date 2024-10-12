

# AppendCellsRequest

Adds new cells after the last row with data in a sheet, inserting new rows into the sheet if necessary.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | **String** | The fields of CellData that should be updated. At least one field must be specified. The root is the CellData; &#39;row.values.&#39; should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. |  [optional] |
|**rows** | [**List&lt;RowData&gt;**](RowData.md) | The data to append. |  [optional] |
|**sheetId** | **Integer** | The sheet ID to append the data to. |  [optional] |



