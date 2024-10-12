# EventGridManagementClient.EventSubscriptionUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  | [optional] 
**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  | [optional] 
**eventDeliverySchema** | **String** | The event delivery schema for the event subscription. | [optional] 
**expirationTimeUtc** | **Date** | Information about the expiration time for the event subscription. | [optional] 
**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  | [optional] 
**labels** | **[String]** | List of user defined labels. | [optional] 
**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  | [optional] 



## Enum: EventDeliverySchemaEnum


* `EventGridSchema` (value: `"EventGridSchema"`)

* `CloudEventV01Schema` (value: `"CloudEventV01Schema"`)

* `CustomInputSchema` (value: `"CustomInputSchema"`)




