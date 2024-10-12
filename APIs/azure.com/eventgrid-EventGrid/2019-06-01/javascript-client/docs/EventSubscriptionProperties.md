# EventGridManagementClient.EventSubscriptionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadLetterDestination** | [**DeadLetterDestination**](DeadLetterDestination.md) |  | [optional] 
**destination** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  | [optional] 
**expirationTimeUtc** | **Date** | Expiration time of the event subscription. | [optional] 
**filter** | [**EventSubscriptionFilter**](EventSubscriptionFilter.md) |  | [optional] 
**labels** | **[String]** | List of user defined labels. | [optional] 
**provisioningState** | **String** | Provisioning state of the event subscription. | [optional] [readonly] 
**retryPolicy** | [**RetryPolicy**](RetryPolicy.md) |  | [optional] 
**topic** | **String** | Name of the topic of the event subscription. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Canceled` (value: `"Canceled"`)

* `Failed` (value: `"Failed"`)

* `AwaitingManualAction` (value: `"AwaitingManualAction"`)




