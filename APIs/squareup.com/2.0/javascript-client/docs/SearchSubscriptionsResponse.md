# SquareConnectApi.SearchSubscriptionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set of subscriptions. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
**errors** | [**[Error]**](Error.md) | Information about errors encountered during the request. | [optional] 
**subscriptions** | [**[Subscription]**](Subscription.md) | The search result. | [optional] 


