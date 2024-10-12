# GoogleDocsApi.TableCell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**[StructuralElement]**](StructuralElement.md) | The content of the cell. | [optional] 
**endIndex** | **Number** | The zero-based end index of this cell, exclusive, in UTF-16 code units. | [optional] 
**startIndex** | **Number** | The zero-based start index of this cell, in UTF-16 code units. | [optional] 
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. A TableCell may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**suggestedTableCellStyleChanges** | [**{String: SuggestedTableCellStyle}**](SuggestedTableCellStyle.md) | The suggested changes to the table cell style, keyed by suggestion ID. | [optional] 
**tableCellStyle** | [**TableCellStyle**](TableCellStyle.md) |  | [optional] 


