

# EventSubscriptionUpdateParameters

Properties of the Event Subscription update

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  |  [optional] |
|**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  |  [optional] |
|**eventDeliverySchema** | [**EventDeliverySchemaEnum**](#EventDeliverySchemaEnum) | The event delivery schema for the event subscription. |  [optional] |
|**expirationTimeUtc** | **OffsetDateTime** | Information about the expiration time for the event subscription. |  [optional] |
|**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  |  [optional] |
|**labels** | **List&lt;String&gt;** | List of user defined labels. |  [optional] |
|**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  |  [optional] |



## Enum: EventDeliverySchemaEnum

| Name | Value |
|---- | -----|
| EVENT_GRID_SCHEMA | &quot;EventGridSchema&quot; |
| CLOUD_EVENT_V01_SCHEMA | &quot;CloudEventV01Schema&quot; |
| CUSTOM_INPUT_SCHEMA | &quot;CustomInputSchema&quot; |



