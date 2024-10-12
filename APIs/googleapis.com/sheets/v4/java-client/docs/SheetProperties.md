

# SheetProperties

Properties of a sheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceSheetProperties** | [**DataSourceSheetProperties**](DataSourceSheetProperties.md) |  |  [optional] |
|**gridProperties** | [**GridProperties**](GridProperties.md) |  |  [optional] |
|**hidden** | **Boolean** | True if the sheet is hidden in the UI, false if it&#39;s visible. |  [optional] |
|**index** | **Integer** | The index of the sheet within the spreadsheet. When adding or updating sheet properties, if this field is excluded then the sheet is added or moved to the end of the sheet list. When updating sheet indices or inserting sheets, movement is considered in \&quot;before the move\&quot; indexes. For example, if there were three sheets (S1, S2, S3) in order to move S1 ahead of S2 the index would have to be set to 2. A sheet index update request is ignored if the requested index is identical to the sheets current index or if the requested new index is equal to the current sheet index + 1. |  [optional] |
|**rightToLeft** | **Boolean** | True if the sheet is an RTL sheet instead of an LTR sheet. |  [optional] |
|**sheetId** | **Integer** | The ID of the sheet. Must be non-negative. This field cannot be changed once set. |  [optional] |
|**sheetType** | [**SheetTypeEnum**](#SheetTypeEnum) | The type of sheet. Defaults to GRID. This field cannot be changed once set. |  [optional] |
|**tabColor** | [**Color**](Color.md) |  |  [optional] |
|**tabColorStyle** | [**ColorStyle**](ColorStyle.md) |  |  [optional] |
|**title** | **String** | The name of the sheet. |  [optional] |



## Enum: SheetTypeEnum

| Name | Value |
|---- | -----|
| SHEET_TYPE_UNSPECIFIED | &quot;SHEET_TYPE_UNSPECIFIED&quot; |
| GRID | &quot;GRID&quot; |
| OBJECT | &quot;OBJECT&quot; |
| DATA_SOURCE | &quot;DATA_SOURCE&quot; |



