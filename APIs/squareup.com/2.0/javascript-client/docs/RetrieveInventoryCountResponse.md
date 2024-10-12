# SquareConnectApi.RetrieveInventoryCountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**[InventoryCount]**](InventoryCount.md) | The current calculated inventory counts for the requested object and locations. | [optional] 
**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. | [optional] 
**errors** | [**[Error]**](Error.md) | Any errors that occurred during the request. | [optional] 


