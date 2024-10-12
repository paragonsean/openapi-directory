

# DataSourceTable

A data source table, which allows the user to import a static table of data from the DataSource into Sheets. This is also known as \"Extract\" in the Sheets editor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnSelectionType** | [**ColumnSelectionTypeEnum**](#ColumnSelectionTypeEnum) | The type to select columns for the data source table. Defaults to SELECTED. |  [optional] |
|**columns** | [**List&lt;DataSourceColumnReference&gt;**](DataSourceColumnReference.md) | Columns selected for the data source table. The column_selection_type must be SELECTED. |  [optional] |
|**dataExecutionStatus** | [**DataExecutionStatus**](DataExecutionStatus.md) |  |  [optional] |
|**dataSourceId** | **String** | The ID of the data source the data source table is associated with. |  [optional] |
|**filterSpecs** | [**List&lt;FilterSpec&gt;**](FilterSpec.md) | Filter specifications in the data source table. |  [optional] |
|**rowLimit** | **Integer** | The limit of rows to return. If not set, a default limit is applied. Please refer to the Sheets editor for the default and max limit. |  [optional] |
|**sortSpecs** | [**List&lt;SortSpec&gt;**](SortSpec.md) | Sort specifications in the data source table. The result of the data source table is sorted based on the sort specifications in order. |  [optional] |



## Enum: ColumnSelectionTypeEnum

| Name | Value |
|---- | -----|
| DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED | &quot;DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED&quot; |
| SELECTED | &quot;SELECTED&quot; |
| SYNC_ALL | &quot;SYNC_ALL&quot; |



