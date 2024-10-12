

# InsertTableColumnsRequest

Inserts columns into a table. Other columns in the table will be resized to fit the new column.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cellLocation** | [**TableCellLocation**](TableCellLocation.md) |  |  [optional] |
|**insertRight** | **Boolean** | Whether to insert new columns to the right of the reference cell location. - &#x60;True&#x60;: insert to the right. - &#x60;False&#x60;: insert to the left. |  [optional] |
|**number** | **Integer** | The number of columns to be inserted. Maximum 20 per request. |  [optional] |
|**tableObjectId** | **String** | The table to insert columns into. |  [optional] |



