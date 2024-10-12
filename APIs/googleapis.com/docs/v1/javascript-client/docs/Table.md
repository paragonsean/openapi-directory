# GoogleDocsApi.Table

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **Number** | Number of columns in the table. It&#39;s possible for a table to be non-rectangular, so some rows may have a different number of cells. | [optional] 
**rows** | **Number** | Number of rows in the table. | [optional] 
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. A Table may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**tableRows** | [**[TableRow]**](TableRow.md) | The contents and style of each row. | [optional] 
**tableStyle** | [**TableStyle**](TableStyle.md) |  | [optional] 


