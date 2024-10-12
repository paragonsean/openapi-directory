

# BatchUpdateValuesByDataFilterResponse

The response when updating a range of values in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**responses** | [**List&lt;UpdateValuesByDataFilterResponse&gt;**](UpdateValuesByDataFilterResponse.md) | The response for each range updated. |  [optional] |
|**spreadsheetId** | **String** | The spreadsheet the updates were applied to. |  [optional] |
|**totalUpdatedCells** | **Integer** | The total number of cells updated. |  [optional] |
|**totalUpdatedColumns** | **Integer** | The total number of columns where at least one cell in the column was updated. |  [optional] |
|**totalUpdatedRows** | **Integer** | The total number of rows where at least one cell in the row was updated. |  [optional] |
|**totalUpdatedSheets** | **Integer** | The total number of sheets where at least one cell in the sheet was updated. |  [optional] |



