# CloudSearchApi.SearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugInfo** | [**ResponseDebugInfo**](ResponseDebugInfo.md) |  | [optional] 
**errorInfo** | [**ErrorInfo**](ErrorInfo.md) |  | [optional] 
**facetResults** | [**[FacetResult]**](FacetResult.md) | Repeated facet results. | [optional] 
**hasMoreResults** | **Boolean** | Whether there are more search results matching the query. | [optional] 
**queryInterpretation** | [**QueryInterpretation**](QueryInterpretation.md) |  | [optional] 
**resultCountEstimate** | **String** | The estimated result count for this query. | [optional] 
**resultCountExact** | **String** | The exact result count for this query. | [optional] 
**resultCounts** | [**ResultCounts**](ResultCounts.md) |  | [optional] 
**results** | [**[SearchResult]**](SearchResult.md) | Results from a search query. | [optional] 
**spellResults** | [**[SpellResult]**](SpellResult.md) | Suggested spelling for the query. | [optional] 
**structuredResults** | [**[StructuredResult]**](StructuredResult.md) | Structured results for the user query. These results are not counted against the page_size. | [optional] 


