

# GoogleCloudRetailV2betaSearchResponse

Response message for SearchService.Search method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedControls** | **List&lt;String&gt;** | The fully qualified resource name of applied [controls](https://cloud.google.com/retail/docs/serving-control-rules). |  [optional] |
|**attributionToken** | **String** | A unique search token. This should be included in the UserEvent logs resulting from this search, which enables accurate attribution of search model performance. |  [optional] |
|**correctedQuery** | **String** | Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search. |  [optional] |
|**experimentInfo** | [**List&lt;GoogleCloudRetailV2betaExperimentInfo&gt;**](GoogleCloudRetailV2betaExperimentInfo.md) | Metadata related to A/B testing Experiment associated with this response. Only exists when an experiment is triggered. |  [optional] |
|**facets** | [**List&lt;GoogleCloudRetailV2betaSearchResponseFacet&gt;**](GoogleCloudRetailV2betaSearchResponseFacet.md) | Results of facets requested by user. |  [optional] |
|**invalidConditionBoostSpecs** | [**List&lt;GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec&gt;**](GoogleCloudRetailV2betaSearchRequestBoostSpecConditionBoostSpec.md) | The invalid SearchRequest.BoostSpec.condition_boost_specs that are not applied during serving. |  [optional] |
|**nextPageToken** | **String** | A token that can be sent as SearchRequest.page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**queryExpansionInfo** | [**GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo**](GoogleCloudRetailV2betaSearchResponseQueryExpansionInfo.md) |  |  [optional] |
|**redirectUri** | **String** | The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only redirect_uri and attribution_token are set in the response. |  [optional] |
|**results** | [**List&lt;GoogleCloudRetailV2betaSearchResponseSearchResult&gt;**](GoogleCloudRetailV2betaSearchResponseSearchResult.md) | A list of matched items. The order represents the ranking. |  [optional] |
|**totalSize** | **Integer** | The estimated total count of matched items irrespective of pagination. The count of results returned by pagination may be less than the total_size that matches. |  [optional] |



