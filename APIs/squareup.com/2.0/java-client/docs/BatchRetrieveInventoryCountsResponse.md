

# BatchRetrieveInventoryCountsResponse



## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**counts** | [**List&lt;InventoryCount&gt;**](InventoryCount.md) | The current calculated inventory counts for the requested objects and locations. |  [optional] |
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |



