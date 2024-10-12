# LgtmApiSpecification.Analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitId** | **String** | The commit identifier. The commit identifier is included only if the same commit was successfully analyzed for all languages. A detailed breakdown of which commit was analyzed for each language is provided in the &#x60;languages&#x60; property.  | [optional] 
**id** | **String** | The analysis identifier. | [optional] 
**languages** | [**[LanguageStats]**](LanguageStats.md) | Per-language information. | [optional] 
**logUrl** | **String** | A page on LGTM to view the logs for this analysis. | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 
**resultsUrl** | **String** | A page on LGTM to view the results of this analysis. | [optional] 


