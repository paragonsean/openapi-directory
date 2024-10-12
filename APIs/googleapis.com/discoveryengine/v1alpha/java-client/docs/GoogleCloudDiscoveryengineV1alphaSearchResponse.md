

# GoogleCloudDiscoveryengineV1alphaSearchResponse

Response message for SearchService.Search method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedControls** | **List&lt;String&gt;** | Controls applied as part of the Control service. |  [optional] |
|**attributionToken** | **String** | A unique search token. This should be included in the UserEvent logs resulting from this search, which enables accurate attribution of search model performance. |  [optional] |
|**correctedQuery** | **String** | Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search. |  [optional] |
|**facets** | [**List&lt;GoogleCloudDiscoveryengineV1alphaSearchResponseFacet&gt;**](GoogleCloudDiscoveryengineV1alphaSearchResponseFacet.md) | Results of facets requested by user. |  [optional] |
|**geoSearchDebugInfo** | [**List&lt;GoogleCloudDiscoveryengineV1alphaSearchResponseGeoSearchDebugInfo&gt;**](GoogleCloudDiscoveryengineV1alphaSearchResponseGeoSearchDebugInfo.md) |  |  [optional] |
|**guidedSearchResult** | [**GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResult**](GoogleCloudDiscoveryengineV1alphaSearchResponseGuidedSearchResult.md) |  |  [optional] |
|**nextPageToken** | **String** | A token that can be sent as SearchRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**queryExpansionInfo** | [**GoogleCloudDiscoveryengineV1alphaSearchResponseQueryExpansionInfo**](GoogleCloudDiscoveryengineV1alphaSearchResponseQueryExpansionInfo.md) |  |  [optional] |
|**redirectUri** | **String** | The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only redirect_uri and attribution_token are set in the response. |  [optional] |
|**results** | [**List&lt;GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult&gt;**](GoogleCloudDiscoveryengineV1alphaSearchResponseSearchResult.md) | A list of matched documents. The order represents the ranking. |  [optional] |
|**summary** | [**GoogleCloudDiscoveryengineV1alphaSearchResponseSummary**](GoogleCloudDiscoveryengineV1alphaSearchResponseSummary.md) |  |  [optional] |
|**totalSize** | **Integer** | The estimated total count of matched items irrespective of pagination. The count of results returned by pagination may be less than the total_size that matches. |  [optional] |



