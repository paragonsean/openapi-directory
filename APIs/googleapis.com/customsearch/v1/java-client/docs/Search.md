

# Search

Response to a custom search request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | **Map&lt;String, Object&gt;** | Metadata and refinements associated with the given search engine, including: * The name of the search engine that was used for the query. * A set of [facet objects](https://developers.google.com/custom-search/docs/refinements#create) (refinements) you can use for refining a search. |  [optional] |
|**items** | [**List&lt;Result&gt;**](Result.md) | The current set of custom search results. |  [optional] |
|**kind** | **String** | Unique identifier for the type of current object. For this API, it is customsearch#search. |  [optional] |
|**promotions** | [**List&lt;Promotion&gt;**](Promotion.md) | The set of [promotions](https://developers.google.com/custom-search/docs/promotions). Present only if the custom search engine&#39;s configuration files define any promotions for the given query. |  [optional] |
|**queries** | [**SearchQueries**](SearchQueries.md) |  |  [optional] |
|**searchInformation** | [**SearchSearchInformation**](SearchSearchInformation.md) |  |  [optional] |
|**spelling** | [**SearchSpelling**](SearchSpelling.md) |  |  [optional] |
|**url** | [**SearchUrl**](SearchUrl.md) |  |  [optional] |



