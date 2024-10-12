# GoogleSheetsApi.CopyPasteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**GridRange**](GridRange.md) |  | [optional] 
**pasteOrientation** | **String** | How that data should be oriented when pasting. | [optional] 
**pasteType** | **String** | What kind of data to paste. | [optional] 
**source** | [**GridRange**](GridRange.md) |  | [optional] 



## Enum: PasteOrientationEnum


* `NORMAL` (value: `"NORMAL"`)

* `TRANSPOSE` (value: `"TRANSPOSE"`)





## Enum: PasteTypeEnum


* `NORMAL` (value: `"PASTE_NORMAL"`)

* `VALUES` (value: `"PASTE_VALUES"`)

* `FORMAT` (value: `"PASTE_FORMAT"`)

* `NO_BORDERS` (value: `"PASTE_NO_BORDERS"`)

* `FORMULA` (value: `"PASTE_FORMULA"`)

* `DATA_VALIDATION` (value: `"PASTE_DATA_VALIDATION"`)

* `CONDITIONAL_FORMATTING` (value: `"PASTE_CONDITIONAL_FORMATTING"`)




