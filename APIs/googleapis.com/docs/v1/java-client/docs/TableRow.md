

# TableRow

The contents and style of a row in a Table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endIndex** | **Integer** | The zero-based end index of this row, exclusive, in UTF-16 code units. |  [optional] |
|**startIndex** | **Integer** | The zero-based start index of this row, in UTF-16 code units. |  [optional] |
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInsertionIds** | **List&lt;String&gt;** | The suggested insertion IDs. A TableRow may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. |  [optional] |
|**suggestedTableRowStyleChanges** | [**Map&lt;String, SuggestedTableRowStyle&gt;**](SuggestedTableRowStyle.md) | The suggested style changes to this row, keyed by suggestion ID. |  [optional] |
|**tableCells** | [**List&lt;TableCell&gt;**](TableCell.md) | The contents and style of each cell in this row. It&#39;s possible for a table to be non-rectangular, so some rows may have a different number of cells than other rows in the same table. |  [optional] |
|**tableRowStyle** | [**TableRowStyle**](TableRowStyle.md) |  |  [optional] |



