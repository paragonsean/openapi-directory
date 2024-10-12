

# SBSubscriptionProperties

Description of Subscription Resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessedAt** | **OffsetDateTime** | Last time there was a receive request to this subscription. |  [optional] [readonly] |
|**autoDeleteOnIdle** | **String** | ISO 8061 timeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes. |  [optional] |
|**countDetails** | [**MessageCountDetails**](MessageCountDetails.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Exact time the message was created. |  [optional] [readonly] |
|**deadLetteringOnFilterEvaluationExceptions** | **Boolean** | Value that indicates whether a subscription has dead letter support on filter evaluation exceptions. |  [optional] |
|**deadLetteringOnMessageExpiration** | **Boolean** | Value that indicates whether a subscription has dead letter support when a message expires. |  [optional] |
|**defaultMessageTimeToLive** | **String** | ISO 8061 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |  [optional] |
|**duplicateDetectionHistoryTimeWindow** | **String** | ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes. |  [optional] |
|**enableBatchedOperations** | **Boolean** | Value that indicates whether server-side batched operations are enabled. |  [optional] |
|**forwardDeadLetteredMessagesTo** | **String** | Queue/Topic name to forward the Dead Letter message |  [optional] |
|**forwardTo** | **String** | Queue/Topic name to forward the messages |  [optional] |
|**lockDuration** | **String** | ISO 8061 lock duration timespan for the subscription. The default value is 1 minute. |  [optional] |
|**maxDeliveryCount** | **Integer** | Number of maximum deliveries. |  [optional] |
|**messageCount** | **Long** | Number of messages. |  [optional] [readonly] |
|**requiresSession** | **Boolean** | Value indicating if a subscription supports the concept of sessions. |  [optional] |
|**status** | **EntityStatus** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The exact time the message was updated. |  [optional] [readonly] |



