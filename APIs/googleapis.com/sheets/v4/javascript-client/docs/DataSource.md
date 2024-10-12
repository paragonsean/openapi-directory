# GoogleSheetsApi.DataSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculatedColumns** | [**[DataSourceColumn]**](DataSourceColumn.md) | All calculated columns in the data source. | [optional] 
**dataSourceId** | **String** | The spreadsheet-scoped unique ID that identifies the data source. Example: 1080547365. | [optional] 
**sheetId** | **Number** | The ID of the Sheet connected with the data source. The field cannot be changed once set. When creating a data source, an associated DATA_SOURCE sheet is also created, if the field is not specified, the ID of the created sheet will be randomly generated. | [optional] 
**spec** | [**DataSourceSpec**](DataSourceSpec.md) |  | [optional] 


