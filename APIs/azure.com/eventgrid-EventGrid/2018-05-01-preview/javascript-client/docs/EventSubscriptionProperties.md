# EventGridManagementClient.EventSubscriptionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  | [optional] 
**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  | [optional] 
**eventDeliverySchema** | **String** | The event delivery schema for the event subscription. | [optional] [default to &#39;InputEventSchema&#39;]
**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  | [optional] 
**labels** | **[String]** | List of user defined labels. | [optional] 
**provisioningState** | **String** | Provisioning state of the event subscription. | [optional] [readonly] 
**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  | [optional] 
**topic** | **String** | Name of the topic of the event subscription. | [optional] [readonly] 



## Enum: EventDeliverySchemaEnum


* `EventGridSchema` (value: `"EventGridSchema"`)

* `InputEventSchema` (value: `"InputEventSchema"`)

* `CloudEventV01Schema` (value: `"CloudEventV01Schema"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Canceled` (value: `"Canceled"`)

* `Failed` (value: `"Failed"`)

* `AwaitingManualAction` (value: `"AwaitingManualAction"`)




