

# TopicProperties

The Topic Properties definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessedAt** | **OffsetDateTime** | Last time the message was sent, or a request was received, for this topic. |  [optional] [readonly] |
|**autoDeleteOnIdle** | **String** | TimeSpan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes. |  [optional] |
|**countDetails** | [**MessageCountDetails**](MessageCountDetails.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Exact time the message was created. |  [optional] [readonly] |
|**defaultMessageTimeToLive** | **String** | Default message time to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself. |  [optional] |
|**duplicateDetectionHistoryTimeWindow** | **String** | TimeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes. |  [optional] |
|**enableBatchedOperations** | **Boolean** | Value that indicates whether server-side batched operations are enabled. |  [optional] |
|**enableExpress** | **Boolean** | Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage. |  [optional] |
|**enablePartitioning** | **Boolean** | Value that indicates whether the topic to be partitioned across multiple message brokers is enabled. |  [optional] |
|**entityAvailabilityStatus** | **EntityAvailabilityStatus** |  |  [optional] |
|**filteringMessagesBeforePublishing** | **Boolean** | Whether messages should be filtered before publishing. |  [optional] |
|**isAnonymousAccessible** | **Boolean** | Value that indicates whether the message is accessible anonymously. |  [optional] |
|**isExpress** | **Boolean** |  |  [optional] |
|**maxSizeInMegabytes** | **Long** | Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. |  [optional] |
|**requiresDuplicateDetection** | **Boolean** | Value indicating if this topic requires duplicate detection. |  [optional] |
|**sizeInBytes** | **Long** | Size of the topic, in bytes. |  [optional] [readonly] |
|**status** | **EntityStatus** |  |  [optional] |
|**subscriptionCount** | **Integer** | Number of subscriptions. |  [optional] [readonly] |
|**supportOrdering** | **Boolean** | Value that indicates whether the topic supports ordering. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The exact time the message was updated. |  [optional] [readonly] |



