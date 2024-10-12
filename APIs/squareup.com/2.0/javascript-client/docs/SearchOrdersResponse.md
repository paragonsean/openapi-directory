# SquareConnectApi.SearchOrdersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 
**errors** | [**[Error]**](Error.md) | [Errors](https://developer.squareup.com/reference/square_2021-08-18/objects/Error) encountered during the search. | [optional] 
**orderEntries** | [**[OrderEntry]**](OrderEntry.md) | A list of [OrderEntries](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderEntry) that fit the query conditions. The list is populated only if &#x60;return_entries&#x60; is set to &#x60;true&#x60; in the request. | [optional] 
**orders** | [**[Order]**](Order.md) | A list of [Order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) objects that match the query conditions. The list is populated only if &#x60;return_entries&#x60; is set to &#x60;false&#x60; in the request. | [optional] 


