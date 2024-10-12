

# Table

A StructuralElement representing a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | **Integer** | Number of columns in the table. It&#39;s possible for a table to be non-rectangular, so some rows may have a different number of cells. |  [optional] |
|**rows** | **Integer** | Number of rows in the table. |  [optional] |
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInsertionIds** | **List&lt;String&gt;** | The suggested insertion IDs. A Table may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. |  [optional] |
|**tableRows** | [**List&lt;TableRow&gt;**](TableRow.md) | The contents and style of each row. |  [optional] |
|**tableStyle** | [**TableStyle**](TableStyle.md) |  |  [optional] |



