

# UpdateTableRowStyleRequest

Updates the TableRowStyle of rows in a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;tableRowStyle&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the minimum row height, set &#x60;fields&#x60; to &#x60;\&quot;min_row_height\&quot;&#x60;. |  [optional] |
|**rowIndices** | **List&lt;Integer&gt;** | The list of zero-based row indices whose style should be updated. If no indices are specified, all rows will be updated. |  [optional] |
|**tableRowStyle** | [**TableRowStyle**](TableRowStyle.md) |  |  [optional] |
|**tableStartLocation** | [**Location**](Location.md) |  |  [optional] |



