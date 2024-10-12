

# CopyPasteRequest

Copies data from the source to the destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | [**GridRange**](GridRange.md) |  |  [optional] |
|**pasteOrientation** | [**PasteOrientationEnum**](#PasteOrientationEnum) | How that data should be oriented when pasting. |  [optional] |
|**pasteType** | [**PasteTypeEnum**](#PasteTypeEnum) | What kind of data to paste. |  [optional] |
|**source** | [**GridRange**](GridRange.md) |  |  [optional] |



## Enum: PasteOrientationEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;NORMAL&quot; |
| TRANSPOSE | &quot;TRANSPOSE&quot; |



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



