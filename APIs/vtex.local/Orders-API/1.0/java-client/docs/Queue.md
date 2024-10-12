

# Queue

Object with information about timeout and message retention.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageRetentionPeriodInSeconds** | **Integer** | Maximum life span of an order update in the feed. When a feed item is on the feed for this period of time, it is removed from the feed. Measured in seconds. |  |
|**visibilityTimeoutInSeconds** | **Integer** | Period of time for which an item becomes invisible after it has been [retrieved](https://developers.vtex.com/vtex-rest-api/reference/feed-v3#getfeedorderstatus1). Measured in seconds. |  |



