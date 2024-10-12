

# TableOfContents

A StructuralElement representing a table of contents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | [**List&lt;StructuralElement&gt;**](StructuralElement.md) | The content of the table of contents. |  [optional] |
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInsertionIds** | **List&lt;String&gt;** | The suggested insertion IDs. A TableOfContents may have multiple insertion IDs if it is a nested suggested change. If empty, then this is not a suggested insertion. |  [optional] |



