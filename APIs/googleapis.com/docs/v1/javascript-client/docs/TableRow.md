# GoogleDocsApi.TableRow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endIndex** | **Number** | The zero-based end index of this row, exclusive, in UTF-16 code units. | [optional] 
**startIndex** | **Number** | The zero-based start index of this row, in UTF-16 code units. | [optional] 
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. A TableRow may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**suggestedTableRowStyleChanges** | [**{String: SuggestedTableRowStyle}**](SuggestedTableRowStyle.md) | The suggested style changes to this row, keyed by suggestion ID. | [optional] 
**tableCells** | [**[TableCell]**](TableCell.md) | The contents and style of each cell in this row. It&#39;s possible for a table to be non-rectangular, so some rows may have a different number of cells than other rows in the same table. | [optional] 
**tableRowStyle** | [**TableRowStyle**](TableRowStyle.md) |  | [optional] 


