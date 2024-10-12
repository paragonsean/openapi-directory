# GoogleSlidesApi.ReplaceAllTextRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containsText** | [**SubstringMatchCriteria**](SubstringMatchCriteria.md) |  | [optional] 
**pageObjectIds** | **[String]** | If non-empty, limits the matches to page elements only on the given pages. Returns a 400 bad request error if given the page object ID of a notes master, or if a page with that object ID doesn&#39;t exist in the presentation. | [optional] 
**replaceText** | **String** | The text that will replace the matched text. | [optional] 


