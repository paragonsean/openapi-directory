

# Feed

Contains the information about a single feed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The unique ID for this feed. This is constructed using the ID of the feed&#39;s provider and an internal ID. This ID can be used in other calls, such as &#x60;/getFeedVersions&#x60; or &#x60;/getLatestFeedVersion&#x60;.  |  |
|**l** | [**Location**](Location.md) |  |  |
|**latest** | [**FeedLatest**](FeedLatest.md) |  |  [optional] |
|**t** | **String** | The title of the feed as it appears on TransitFeeds.com |  |
|**ty** | [**TyEnum**](#TyEnum) | The type of feed (such as GTFS or GTFS-realtime). |  |
|**u** | [**FeedU**](FeedU.md) |  |  [optional] |



## Enum: TyEnum

| Name | Value |
|---- | -----|
| GTFS | &quot;gtfs&quot; |
| GTFSREALTIME | &quot;gtfsrealtime&quot; |



