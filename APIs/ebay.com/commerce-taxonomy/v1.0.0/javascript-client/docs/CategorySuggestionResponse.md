# TaxonomyApi.CategorySuggestionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categorySuggestions** | [**[CategorySuggestion]**](CategorySuggestion.md) | Contains details about one or more suggested categories that correspond to the provided keywords. The array of suggested categories is sorted in order of eBay&#39;s confidence of the relevance of each category (the first category is the most relevant). Important: This call is not supported in the Sandbox environment. It will return a response payload in which the categoryName fields contain random or boilerplate text regardless of the query submitted. | [optional] 
**categoryTreeId** | **String** | The unique identifier of the eBay category tree from which suggestions are returned. | [optional] 
**categoryTreeVersion** | **String** | The version of the category tree identified by categoryTreeId. It&#39;s a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls. | [optional] 


