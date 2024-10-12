

# UpdateRowRequest

Request message for TablesService.UpdateRow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**row** | [**Row**](Row.md) |  |  [optional] |
|**updateMask** | **String** | The list of fields to update. |  [optional] |
|**view** | [**ViewEnum**](#ViewEnum) | Optional. Column key to use for values in the row. Defaults to user entered name. |  [optional] |



## Enum: ViewEnum

| Name | Value |
|---- | -----|
| VIEW_UNSPECIFIED | &quot;VIEW_UNSPECIFIED&quot; |
| COLUMN_ID_VIEW | &quot;COLUMN_ID_VIEW&quot; |



