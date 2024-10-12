

# PageBreak

A ParagraphElement representing a page break. A page break makes the subsequent text start at the top of the next page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInsertionIds** | **List&lt;String&gt;** | The suggested insertion IDs. A PageBreak may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. |  [optional] |
|**suggestedTextStyleChanges** | [**Map&lt;String, SuggestedTextStyle&gt;**](SuggestedTextStyle.md) | The suggested text style changes to this PageBreak, keyed by suggestion ID. |  [optional] |
|**textStyle** | [**TextStyle**](TextStyle.md) |  |  [optional] |



