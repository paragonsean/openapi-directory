

# EventSubscriptionUpdateParameters

Properties of the Event Subscription update

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  |  [optional] |
|**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  |  [optional] |
|**expirationTimeUtc** | **OffsetDateTime** | Information about the expiration time for the event subscription. |  [optional] |
|**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  |  [optional] |
|**labels** | **List&lt;String&gt;** | List of user defined labels. |  [optional] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |



