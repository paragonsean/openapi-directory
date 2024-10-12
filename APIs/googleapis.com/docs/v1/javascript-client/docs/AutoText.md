# GoogleDocsApi.AutoText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. An AutoText may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**suggestedTextStyleChanges** | [**{String: SuggestedTextStyle}**](SuggestedTextStyle.md) | The suggested text style changes to this AutoText, keyed by suggestion ID. | [optional] 
**textStyle** | [**TextStyle**](TextStyle.md) |  | [optional] 
**type** | **String** | The type of this auto text. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `PAGE_NUMBER` (value: `"PAGE_NUMBER"`)

* `PAGE_COUNT` (value: `"PAGE_COUNT"`)




