

# DuplicateSheetRequest

Duplicates the contents of a sheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**insertSheetIndex** | **Integer** | The zero-based index where the new sheet should be inserted. The index of all sheets after this are incremented. |  [optional] |
|**newSheetId** | **Integer** | If set, the ID of the new sheet. If not set, an ID is chosen. If set, the ID must not conflict with any existing sheet ID. If set, it must be non-negative. |  [optional] |
|**newSheetName** | **String** | The name of the new sheet. If empty, a new name is chosen for you. |  [optional] |
|**sourceSheetId** | **Integer** | The sheet to duplicate. If the source sheet is of DATA_SOURCE type, its backing DataSource is also duplicated and associated with the new copy of the sheet. No data execution is triggered, the grid data of this sheet is also copied over but only available after the batch request completes. |  [optional] |



