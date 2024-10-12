

# BatchClearValuesByDataFilterResponse

The response when clearing a range of values selected with DataFilters in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clearedRanges** | **List&lt;String&gt;** | The ranges that were cleared, in [A1 notation](/sheets/api/guides/concepts#cell). If the requests are for an unbounded range or a ranger larger than the bounds of the sheet, this is the actual ranges that were cleared, bounded to the sheet&#39;s limits. |  [optional] |
|**spreadsheetId** | **String** | The spreadsheet the updates were applied to. |  [optional] |



