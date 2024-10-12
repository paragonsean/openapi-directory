

# SearchResponse

The search API response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**debugInfo** | [**ResponseDebugInfo**](ResponseDebugInfo.md) |  |  [optional] |
|**errorInfo** | [**ErrorInfo**](ErrorInfo.md) |  |  [optional] |
|**facetResults** | [**List&lt;FacetResult&gt;**](FacetResult.md) | Repeated facet results. |  [optional] |
|**hasMoreResults** | **Boolean** | Whether there are more search results matching the query. |  [optional] |
|**queryInterpretation** | [**QueryInterpretation**](QueryInterpretation.md) |  |  [optional] |
|**resultCountEstimate** | **String** | The estimated result count for this query. |  [optional] |
|**resultCountExact** | **String** | The exact result count for this query. |  [optional] |
|**resultCounts** | [**ResultCounts**](ResultCounts.md) |  |  [optional] |
|**results** | [**List&lt;SearchResult&gt;**](SearchResult.md) | Results from a search query. |  [optional] |
|**spellResults** | [**List&lt;SpellResult&gt;**](SpellResult.md) | Suggested spelling for the query. |  [optional] |
|**structuredResults** | [**List&lt;StructuredResult&gt;**](StructuredResult.md) | Structured results for the user query. These results are not counted against the page_size. |  [optional] |



