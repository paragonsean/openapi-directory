# GoogleDocsApi.RichLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**richLinkId** | **String** | Output only. The ID of this link. | [optional] [readonly] 
**richLinkProperties** | [**RichLinkProperties**](RichLinkProperties.md) |  | [optional] 
**suggestedDeletionIds** | **[String]** | IDs for suggestions that remove this link from the document. A RichLink might have multiple deletion IDs if, for example, multiple users suggest deleting it. If empty, then this person link isn&#39;t suggested for deletion. | [optional] 
**suggestedInsertionIds** | **[String]** | IDs for suggestions that insert this link into the document. A RichLink might have multiple insertion IDs if it&#39;s a nested suggested change (a suggestion within a suggestion made by a different user, for example). If empty, then this person link isn&#39;t a suggested insertion. | [optional] 
**suggestedTextStyleChanges** | [**{String: SuggestedTextStyle}**](SuggestedTextStyle.md) | The suggested text style changes to this RichLink, keyed by suggestion ID. | [optional] 
**textStyle** | [**TextStyle**](TextStyle.md) |  | [optional] 


