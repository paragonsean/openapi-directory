# SquareConnectApi.ListSubscriptionEventsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **String** | When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set of events. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] 
**errors** | [**[Error]**](Error.md) | Information about errors encountered during the request. | [optional] 
**subscriptionEvents** | [**[SubscriptionEvent]**](SubscriptionEvent.md) | The &#x60;SubscriptionEvents&#x60; retrieved. | [optional] 


