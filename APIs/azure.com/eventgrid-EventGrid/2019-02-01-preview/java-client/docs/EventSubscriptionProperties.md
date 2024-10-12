

# EventSubscriptionProperties

Properties of the Event Subscription

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  |  [optional] |
|**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  |  [optional] |
|**eventDeliverySchema** | [**EventDeliverySchemaEnum**](#EventDeliverySchemaEnum) | The event delivery schema for the event subscription. |  [optional] |
|**expirationTimeUtc** | **OffsetDateTime** | Expiration time of the event subscription. |  [optional] |
|**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  |  [optional] |
|**labels** | **List&lt;String&gt;** | List of user defined labels. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the event subscription. |  [optional] [readonly] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |
|**topic** | **String** | Name of the topic of the event subscription. |  [optional] [readonly] |



## Enum: EventDeliverySchemaEnum

| Name | Value |
|---- | -----|
| EVENT_GRID_SCHEMA | &quot;EventGridSchema&quot; |
| CLOUD_EVENT_V01_SCHEMA | &quot;CloudEventV01Schema&quot; |
| CUSTOM_INPUT_SCHEMA | &quot;CustomInputSchema&quot; |



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



