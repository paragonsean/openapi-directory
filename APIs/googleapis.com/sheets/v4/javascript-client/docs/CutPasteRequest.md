# GoogleSheetsApi.CutPasteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**GridCoordinate**](GridCoordinate.md) |  | [optional] 
**pasteType** | **String** | What kind of data to paste. All the source data will be cut, regardless of what is pasted. | [optional] 
**source** | [**GridRange**](GridRange.md) |  | [optional] 



## Enum: PasteTypeEnum


* `NORMAL` (value: `"PASTE_NORMAL"`)

* `VALUES` (value: `"PASTE_VALUES"`)

* `FORMAT` (value: `"PASTE_FORMAT"`)

* `NO_BORDERS` (value: `"PASTE_NO_BORDERS"`)

* `FORMULA` (value: `"PASTE_FORMULA"`)

* `DATA_VALIDATION` (value: `"PASTE_DATA_VALIDATION"`)

* `CONDITIONAL_FORMATTING` (value: `"PASTE_CONDITIONAL_FORMATTING"`)




