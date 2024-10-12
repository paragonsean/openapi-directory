# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaSearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedControls** | **[String]** | Controls applied as part of the Control service. | [optional] 
**attributionToken** | **String** | A unique search token. This should be included in the UserEvent logs resulting from this search, which enables accurate attribution of search model performance. | [optional] 
**correctedQuery** | **String** | Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search. | [optional] 
**facets** | [**[GoogleCloudDiscoveryengineV1betaSearchResponseFacet]**](GoogleCloudDiscoveryengineV1betaSearchResponseFacet.md) | Results of facets requested by user. | [optional] 
**geoSearchDebugInfo** | [**[GoogleCloudDiscoveryengineV1betaSearchResponseGeoSearchDebugInfo]**](GoogleCloudDiscoveryengineV1betaSearchResponseGeoSearchDebugInfo.md) |  | [optional] 
**guidedSearchResult** | [**GoogleCloudDiscoveryengineV1betaSearchResponseGuidedSearchResult**](GoogleCloudDiscoveryengineV1betaSearchResponseGuidedSearchResult.md) |  | [optional] 
**nextPageToken** | **String** | A token that can be sent as SearchRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**queryExpansionInfo** | [**GoogleCloudDiscoveryengineV1betaSearchResponseQueryExpansionInfo**](GoogleCloudDiscoveryengineV1betaSearchResponseQueryExpansionInfo.md) |  | [optional] 
**redirectUri** | **String** | The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only redirect_uri and attribution_token are set in the response. | [optional] 
**results** | [**[GoogleCloudDiscoveryengineV1betaSearchResponseSearchResult]**](GoogleCloudDiscoveryengineV1betaSearchResponseSearchResult.md) | A list of matched documents. The order represents the ranking. | [optional] 
**summary** | [**GoogleCloudDiscoveryengineV1betaSearchResponseSummary**](GoogleCloudDiscoveryengineV1betaSearchResponseSummary.md) |  | [optional] 
**totalSize** | **Number** | The estimated total count of matched items irrespective of pagination. The count of results returned by pagination may be less than the total_size that matches. | [optional] 


