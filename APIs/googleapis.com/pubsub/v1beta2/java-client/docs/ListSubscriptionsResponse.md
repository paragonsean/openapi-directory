

# ListSubscriptionsResponse

Response for the `ListSubscriptions` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If not empty, indicates that there may be more subscriptions that match the request; this value should be passed in a new &#x60;ListSubscriptionsRequest&#x60; to get more subscriptions. |  [optional] |
|**subscriptions** | [**List&lt;Subscription&gt;**](Subscription.md) | The subscriptions that match the request. |  [optional] |



