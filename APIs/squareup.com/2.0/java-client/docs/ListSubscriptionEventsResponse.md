

# ListSubscriptionEventsResponse

Defines the fields that are included in the response from the [ListSubscriptionEvents](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/list-subscription-events) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set of events. If empty, this is the final response.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**subscriptionEvents** | [**List&lt;SubscriptionEvent&gt;**](SubscriptionEvent.md) | The &#x60;SubscriptionEvents&#x60; retrieved. |  [optional] |



