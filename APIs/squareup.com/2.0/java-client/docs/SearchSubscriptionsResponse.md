

# SearchSubscriptionsResponse

Defines the fields that are included in the response from the [SearchSubscriptions](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/search-subscriptions) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set of subscriptions. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**subscriptions** | [**List&lt;Subscription&gt;**](Subscription.md) | The search result. |  [optional] |



