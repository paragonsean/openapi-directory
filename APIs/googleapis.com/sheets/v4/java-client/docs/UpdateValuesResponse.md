

# UpdateValuesResponse

The response when updating a range of values in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spreadsheetId** | **String** | The spreadsheet the updates were applied to. |  [optional] |
|**updatedCells** | **Integer** | The number of cells updated. |  [optional] |
|**updatedColumns** | **Integer** | The number of columns where at least one cell in the column was updated. |  [optional] |
|**updatedData** | [**ValueRange**](ValueRange.md) |  |  [optional] |
|**updatedRange** | **String** | The range (in A1 notation) that updates were applied to. |  [optional] |
|**updatedRows** | **Integer** | The number of rows where at least one cell in the row was updated. |  [optional] |



