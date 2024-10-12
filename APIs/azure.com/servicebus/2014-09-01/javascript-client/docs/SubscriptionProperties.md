# ServiceBusManagementClient.SubscriptionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessedAt** | **Date** | Last time there was a receive request to this subscription. | [optional] [readonly] 
**autoDeleteOnIdle** | **String** | TimeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes. | [optional] 
**countDetails** | [**MessageCountDetails**](MessageCountDetails.md) |  | [optional] 
**createdAt** | **Date** | Exact time the message was created. | [optional] [readonly] 
**deadLetteringOnFilterEvaluationExceptions** | **Boolean** | Value that indicates whether a subscription has dead letter support on filter evaluation exceptions. | [optional] 
**deadLetteringOnMessageExpiration** | **Boolean** | Value that indicates whether a subscription has dead letter support when a message expires. | [optional] 
**defaultMessageTimeToLive** | **String** | Default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. | [optional] 
**enableBatchedOperations** | **Boolean** | Value that indicates whether server-side batched operations are enabled. | [optional] 
**entityAvailabilityStatus** | [**EntityAvailabilityStatus**](EntityAvailabilityStatus.md) |  | [optional] 
**isReadOnly** | **Boolean** | Value that indicates whether the entity description is read-only. | [optional] 
**lockDuration** | **String** | The lock duration time span for the subscription. | [optional] 
**maxDeliveryCount** | **Number** | Number of maximum deliveries. | [optional] 
**messageCount** | **Number** | Number of messages. | [optional] [readonly] 
**requiresSession** | **Boolean** | Value indicating if a subscription supports the concept of sessions. | [optional] 
**status** | [**EntityStatus**](EntityStatus.md) |  | [optional] 
**updatedAt** | **Date** | The exact time the message was updated. | [optional] [readonly] 


