# ServiceBusManagementClient.QueueProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessedAt** | **Date** | Last time a message was sent, or the last time there was a receive request to this queue. | [optional] [readonly] 
**autoDeleteOnIdle** | **String** | the TimeSpan idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes. | [optional] 
**countDetails** | [**MessageCountDetails**](MessageCountDetails.md) |  | [optional] 
**createdAt** | **Date** | The exact time the message was created. | [optional] [readonly] 
**deadLetteringOnMessageExpiration** | **Boolean** | A value that indicates whether this queue has dead letter support when a message expires. | [optional] 
**defaultMessageTimeToLive** | **String** | The default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. | [optional] 
**duplicateDetectionHistoryTimeWindow** | **String** | TimeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes. | [optional] 
**enableBatchedOperations** | **Boolean** | A value that indicates whether server-side batched operations are enabled. | [optional] 
**enableExpress** | **Boolean** | A value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage. | [optional] 
**enablePartitioning** | **Boolean** | A value that indicates whether the queue is to be partitioned across multiple message brokers. | [optional] 
**entityAvailabilityStatus** | [**EntityAvailabilityStatus**](EntityAvailabilityStatus.md) |  | [optional] 
**isAnonymousAccessible** | **Boolean** | A value that indicates whether the message is accessible anonymously. | [optional] 
**lockDuration** | **String** | The duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute. | [optional] 
**maxDeliveryCount** | **Number** | The maximum delivery count. A message is automatically deadlettered after this number of deliveries. | [optional] 
**maxSizeInMegabytes** | **Number** | The maximum size of the queue in megabytes, which is the size of memory allocated for the queue. | [optional] 
**messageCount** | **Number** | The number of messages in the queue. | [optional] [readonly] 
**requiresDuplicateDetection** | **Boolean** | A value indicating if this queue requires duplicate detection. | [optional] 
**requiresSession** | **Boolean** | A value that indicates whether the queue supports the concept of sessions. | [optional] 
**sizeInBytes** | **Number** | The size of the queue, in bytes. | [optional] [readonly] 
**status** | [**EntityStatus**](EntityStatus.md) |  | [optional] 
**supportOrdering** | **Boolean** | A value that indicates whether the queue supports ordering. | [optional] 
**updatedAt** | **Date** | The exact time the message was updated. | [optional] [readonly] 


