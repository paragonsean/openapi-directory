# SquareConnectApi.SearchOrdersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 
**limit** | **Number** | The maximum number of results to be returned in a single page. It is possible to receive fewer results than the specified limit on a given page.  Default: &#x60;500&#x60; | [optional] 
**locationIds** | **[String]** | The location IDs for the orders to query. All locations must belong to the same merchant.  Min: 1 location ID.  Max: 10 location IDs. | [optional] 
**query** | [**SearchOrdersQuery**](SearchOrdersQuery.md) |  | [optional] 
**returnEntries** | **Boolean** | A Boolean that controls the format of the search results. If &#x60;true&#x60;, &#x60;SearchOrders&#x60; returns [OrderEntry](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) objects. If &#x60;false&#x60;, &#x60;SearchOrders&#x60; returns complete order objects.  Default: &#x60;false&#x60;. | [optional] 


