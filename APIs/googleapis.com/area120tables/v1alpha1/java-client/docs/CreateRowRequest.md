

# CreateRowRequest

Request message for TablesService.CreateRow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parent** | **String** | Required. The parent table where this row will be created. Format: tables/{table} |  [optional] |
|**row** | [**Row**](Row.md) |  |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | Optional. Column key to use for values in the row. Defaults to user entered name. |  [optional] |



## Enum: ViewEnum

| Name | Value |
|---- | -----|
| VIEW_UNSPECIFIED | &quot;VIEW_UNSPECIFIED&quot; |
| COLUMN_ID_VIEW | &quot;COLUMN_ID_VIEW&quot; |



