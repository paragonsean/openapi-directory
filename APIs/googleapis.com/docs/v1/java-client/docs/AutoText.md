

# AutoText

A ParagraphElement representing a spot in the text that's dynamically replaced with content that can change over time, like a page number.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suggestedDeletionIds** | **List&lt;String&gt;** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. |  [optional] |
|**suggestedInsertionIds** | **List&lt;String&gt;** | The suggested insertion IDs. An AutoText may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. |  [optional] |
|**suggestedTextStyleChanges** | [**Map&lt;String, SuggestedTextStyle&gt;**](SuggestedTextStyle.md) | The suggested text style changes to this AutoText, keyed by suggestion ID. |  [optional] |
|**textStyle** | [**TextStyle**](TextStyle.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this auto text. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PAGE_NUMBER | &quot;PAGE_NUMBER&quot; |
| PAGE_COUNT | &quot;PAGE_COUNT&quot; |



