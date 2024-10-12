

# BatchClearValuesResponse

The response when clearing a range of values in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clearedRanges** | **List&lt;String&gt;** | The ranges that were cleared, in A1 notation. If the requests are for an unbounded range or a ranger larger than the bounds of the sheet, this is the actual ranges that were cleared, bounded to the sheet&#39;s limits. |  [optional] |
|**spreadsheetId** | **String** | The spreadsheet the updates were applied to. |  [optional] |



