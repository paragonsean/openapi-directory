# GoogleDocsApi.PageBreak

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. A PageBreak may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**suggestedTextStyleChanges** | [**{String: SuggestedTextStyle}**](SuggestedTextStyle.md) | The suggested text style changes to this PageBreak, keyed by suggestion ID. | [optional] 
**textStyle** | [**TextStyle**](TextStyle.md) |  | [optional] 


