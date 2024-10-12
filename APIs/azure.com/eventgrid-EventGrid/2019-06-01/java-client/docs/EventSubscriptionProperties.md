

# EventSubscriptionProperties

Properties of the Event Subscription

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  |  [optional] |
|**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  |  [optional] |
|**expirationTimeUtc** | **OffsetDateTime** | Expiration time of the event subscription. |  [optional] |
|**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  |  [optional] |
|**labels** | **List&lt;String&gt;** | List of user defined labels. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the event subscription. |  [optional] [readonly] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |
|**topic** | **String** | Name of the topic of the event subscription. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |
| AWAITING_MANUAL_ACTION | &quot;AwaitingManualAction&quot; |



