# BrowseApi.SearchPagedCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoCorrections** | [**AutoCorrections**](AutoCorrections.md) |  | [optional] 
**href** | **String** | The URI of the current page of results. The following example of the search method returns items 1 thru 5 from the list of items found. https://api.ebay.com/buy/v1/item_summary/search?q&#x3D;shirt&amp;amp;limit&#x3D;5&amp;amp;offset&#x3D;0. | [optional] 
**itemSummaries** | [**[ItemSummary]**](ItemSummary.md) | An array of the items on this page. The items are sorted according to the sorting method specified in the request. | [optional] 
**limit** | **Number** | The value of the limit parameter submitted in the request, which is the maximum number of items to return on a page, from the result set. A result set is the complete set of items returned by the method. | [optional] 
**next** | **String** | The URI for the next page of results. This value is returned if there is an additional page of results to return from the result set. The following example of the search method returns items 5 thru 10 from the list of items found. https://api.ebay.com/buy/v1/item_summary/search?query&#x3D;t-shirts&amp;amp;limit&#x3D;5&amp;amp;offset&#x3D;10 | [optional] 
**offset** | **Number** | This value indicates the offset used for current page of items being returned. Assume the initial request used an offset of 0 and a limit of 3. Then in the first page of results, this value would be 0, and items 1-3 are returned. For the second page, this value is 3 and so on. | [optional] 
**prev** | **String** | The URI for the previous page of results. This is returned if there is a previous page of results from the result set. The following example of the search method returns items 1 thru 5 from the list of items found, which would be the first set of items returned. https://api.ebay.com/buy/v1/item_summary/search?query&#x3D;t-shirts&amp;amp;limit&#x3D;5&amp;amp;offset&#x3D;0 | [optional] 
**refinement** | [**Refinement**](Refinement.md) |  | [optional] 
**total** | **Number** | The total number of items that match the input criteria. | [optional] 
**warnings** | [**[Error]**](Error.md) | The container with all the warnings for the request. | [optional] 


