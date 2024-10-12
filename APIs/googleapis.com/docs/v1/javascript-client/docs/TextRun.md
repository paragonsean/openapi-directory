# GoogleDocsApi.TextRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The text of this run. Any non-text elements in the run are replaced with the Unicode character U+E907. | [optional] 
**suggestedDeletionIds** | **[String]** | The suggested deletion IDs. If empty, then there are no suggested deletions of this content. | [optional] 
**suggestedInsertionIds** | **[String]** | The suggested insertion IDs. A TextRun may have multiple insertion IDs if it&#39;s a nested suggested change. If empty, then this is not a suggested insertion. | [optional] 
**suggestedTextStyleChanges** | [**{String: SuggestedTextStyle}**](SuggestedTextStyle.md) | The suggested text style changes to this run, keyed by suggestion ID. | [optional] 
**textStyle** | [**TextStyle**](TextStyle.md) |  | [optional] 


