# GoogleDocsApi.InlineObjectElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inlineObjectId** | **String** | The ID of the InlineObject this element contains. | [optional] 
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. An InlineObjectElement may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**suggestedTextStyleChanges** | [**{String: SuggestedTextStyle}**](SuggestedTextStyle.md) | The suggested text style changes to this InlineObject, keyed by suggestion ID. | [optional] 
**textStyle** | [**TextStyle**](TextStyle.md) |  | [optional] 


