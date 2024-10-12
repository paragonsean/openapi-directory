

# SearchCatalogItemsResponse

Defines the response body returned from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | Pagination token used in the next request to return more of the search result. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**items** | [**List&lt;CatalogObject&gt;**](CatalogObject.md) | Returned items matching the specified query expressions. |  [optional] |
|**matchedVariationIds** | **List&lt;String&gt;** | Ids of returned item variations matching the specified query expression. |  [optional] |



