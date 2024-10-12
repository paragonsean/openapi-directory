

# InsertTableRowsRequest

Inserts rows into a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cellLocation** | [**TableCellLocation**](TableCellLocation.md) |  |  [optional] |
|**insertBelow** | **Boolean** | Whether to insert new rows below the reference cell location. - &#x60;True&#x60;: insert below the cell. - &#x60;False&#x60;: insert above the cell. |  [optional] |
|**number** | **Integer** | The number of rows to be inserted. Maximum 20 per request. |  [optional] |
|**tableObjectId** | **String** | The table to insert rows into. |  [optional] |



