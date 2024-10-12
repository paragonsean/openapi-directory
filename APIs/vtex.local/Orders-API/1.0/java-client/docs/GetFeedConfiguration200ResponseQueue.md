

# GetFeedConfiguration200ResponseQueue

Information that define the functioning of the queue.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageRetentionPeriodInSeconds** | **Integer** | Maximum life span of an order update after it gets to the feed. When a feed item is on the feed for this period of time, it is removed from the feed. Measured in seconds. |  [optional] |
|**visibilityTimeoutInSeconds** | **Integer** | Period of time for which an item is not visible in the feed after it has been retrieved with the Get feed items request. Measured in seconds. |  [optional] |



