# GoogleSheetsApi.DataSourceTable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnSelectionType** | **String** | The type to select columns for the data source table. Defaults to SELECTED. | [optional] 
**columns** | [**[DataSourceColumnReference]**](DataSourceColumnReference.md) | Columns selected for the data source table. The column_selection_type must be SELECTED. | [optional] 
**dataExecutionStatus** | [**DataExecutionStatus**](DataExecutionStatus.md) |  | [optional] 
**dataSourceId** | **String** | The ID of the data source the data source table is associated with. | [optional] 
**filterSpecs** | [**[FilterSpec]**](FilterSpec.md) | Filter specifications in the data source table. | [optional] 
**rowLimit** | **Number** | The limit of rows to return. If not set, a default limit is applied. Please refer to the Sheets editor for the default and max limit. | [optional] 
**sortSpecs** | [**[SortSpec]**](SortSpec.md) | Sort specifications in the data source table. The result of the data source table is sorted based on the sort specifications in order. | [optional] 



## Enum: ColumnSelectionTypeEnum


* `DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED` (value: `"DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED"`)

* `SELECTED` (value: `"SELECTED"`)

* `SYNC_ALL` (value: `"SYNC_ALL"`)




