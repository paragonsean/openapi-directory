

# PasteDataRequest

Inserts data into the spreadsheet starting at the specified coordinate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coordinate** | [**GridCoordinate**](GridCoordinate.md) |  |  [optional] |
|**data** | **String** | The data to insert. |  [optional] |
|**delimiter** | **String** | The delimiter in the data. |  [optional] |
|**html** | **Boolean** | True if the data is HTML. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | How the data should be pasted. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;PASTE_NORMAL&quot; |
| VALUES | &quot;PASTE_VALUES&quot; |
| FORMAT | &quot;PASTE_FORMAT&quot; |
| NO_BORDERS | &quot;PASTE_NO_BORDERS&quot; |
| FORMULA | &quot;PASTE_FORMULA&quot; |
| DATA_VALIDATION | &quot;PASTE_DATA_VALIDATION&quot; |
| CONDITIONAL_FORMATTING | &quot;PASTE_CONDITIONAL_FORMATTING&quot; |



