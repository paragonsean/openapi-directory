# GoogleDocsApi.Person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**personId** | **String** | Output only. The unique ID of this link. | [optional] [readonly] 
**personProperties** | [**PersonProperties**](PersonProperties.md) |  | [optional] 
**suggestedDeletionIds** | **[String]** | IDs for suggestions that remove this person link from the document. A Person might have multiple deletion IDs if, for example, multiple users suggest deleting it. If empty, then this person link isn&#39;t suggested for deletion. | [optional] 
**suggestedInsertionIds** | **[String]** | IDs for suggestions that insert this person link into the document. A Person might have multiple insertion IDs if it&#39;s a nested suggested change (a suggestion within a suggestion made by a different user, for example). If empty, then this person link isn&#39;t a suggested insertion. | [optional] 
**suggestedTextStyleChanges** | [**{String: SuggestedTextStyle}**](SuggestedTextStyle.md) | The suggested text style changes to this Person, keyed by suggestion ID. | [optional] 
**textStyle** | [**TextStyle**](TextStyle.md) |  | [optional] 


