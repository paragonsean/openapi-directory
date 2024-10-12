

# ListTopicSubscriptionsResponse

Response for the `ListTopicSubscriptions` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Optional. If not empty, indicates that there may be more subscriptions that match the request; this value should be passed in a new &#x60;ListTopicSubscriptionsRequest&#x60; to get more subscriptions. |  [optional] |
|**subscriptions** | **List&lt;String&gt;** | Optional. The names of subscriptions attached to the topic specified in the request. |  [optional] |



