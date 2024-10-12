# SquareConnectApi.SearchCatalogItemsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | Pagination token used in the next request to return more of the search result. | [optional] 
**errors** | [**[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 
**items** | [**[CatalogObject]**](CatalogObject.md) | Returned items matching the specified query expressions. | [optional] 
**matchedVariationIds** | **[String]** | Ids of returned item variations matching the specified query expression. | [optional] 


