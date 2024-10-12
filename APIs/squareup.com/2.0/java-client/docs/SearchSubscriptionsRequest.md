

# SearchSubscriptionsRequest

Defines parameters in a [SearchSubscriptions](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/search-subscriptions) endpoint request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**limit** | **Integer** | The upper limit on the number of subscriptions to return in the response.  Default: &#x60;200&#x60; |  [optional] |
|**query** | [**SearchSubscriptionsQuery**](SearchSubscriptionsQuery.md) |  |  [optional] |



