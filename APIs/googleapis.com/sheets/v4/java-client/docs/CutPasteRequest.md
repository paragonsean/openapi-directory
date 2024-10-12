

# CutPasteRequest

Moves data from the source to the destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**GridCoordinate**](GridCoordinate.md) |  |  [optional] |
|**pasteType** | [**PasteTypeEnum**](#PasteTypeEnum) | What kind of data to paste. All the source data will be cut, regardless of what is pasted. |  [optional] |
|**source** | [**GridRange**](GridRange.md) |  |  [optional] |



## Enum: PasteTypeEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;PASTE_NORMAL&quot; |
| VALUES | &quot;PASTE_VALUES&quot; |
| FORMAT | &quot;PASTE_FORMAT&quot; |
| NO_BORDERS | &quot;PASTE_NO_BORDERS&quot; |
| FORMULA | &quot;PASTE_FORMULA&quot; |
| DATA_VALIDATION | &quot;PASTE_DATA_VALIDATION&quot; |
| CONDITIONAL_FORMATTING | &quot;PASTE_CONDITIONAL_FORMATTING&quot; |



