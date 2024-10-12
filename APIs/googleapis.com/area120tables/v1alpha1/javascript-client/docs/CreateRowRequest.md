# Area120TablesApi.CreateRowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **String** | Required. The parent table where this row will be created. Format: tables/{table} | [optional] 
**row** | [**Row**](Row.md) |  | [optional] 
**view** | **String** | Optional. Column key to use for values in the row. Defaults to user entered name. | [optional] 



## Enum: ViewEnum


* `VIEW_UNSPECIFIED` (value: `"VIEW_UNSPECIFIED"`)

* `COLUMN_ID_VIEW` (value: `"COLUMN_ID_VIEW"`)




