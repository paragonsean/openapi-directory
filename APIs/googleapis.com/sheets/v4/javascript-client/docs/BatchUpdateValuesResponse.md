# GoogleSheetsApi.BatchUpdateValuesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**[UpdateValuesResponse]**](UpdateValuesResponse.md) | One UpdateValuesResponse per requested range, in the same order as the requests appeared. | [optional] 
**spreadsheetId** | **String** | The spreadsheet the updates were applied to. | [optional] 
**totalUpdatedCells** | **Number** | The total number of cells updated. | [optional] 
**totalUpdatedColumns** | **Number** | The total number of columns where at least one cell in the column was updated. | [optional] 
**totalUpdatedRows** | **Number** | The total number of rows where at least one cell in the row was updated. | [optional] 
**totalUpdatedSheets** | **Number** | The total number of sheets where at least one cell in the sheet was updated. | [optional] 


