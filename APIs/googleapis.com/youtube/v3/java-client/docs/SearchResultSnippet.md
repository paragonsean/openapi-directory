

# SearchResultSnippet

Basic details about a search result, including title, description and thumbnails of the item referenced by the search result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | The value that YouTube uses to uniquely identify the channel that published the resource that the search result identifies. |  [optional] |
|**channelTitle** | **String** | The title of the channel that published the resource that the search result identifies. |  [optional] |
|**description** | **String** | A description of the search result. |  [optional] |
|**liveBroadcastContent** | [**LiveBroadcastContentEnum**](#LiveBroadcastContentEnum) | It indicates if the resource (video or channel) has upcoming/active live broadcast content. Or it&#39;s \&quot;none\&quot; if there is not any upcoming/active live broadcasts. |  [optional] |
|**publishedAt** | **OffsetDateTime** | The creation date and time of the resource that the search result identifies. |  [optional] |
|**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  |  [optional] |
|**title** | **String** | The title of the search result. |  [optional] |



## Enum: LiveBroadcastContentEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| UPCOMING | &quot;upcoming&quot; |
| LIVE | &quot;live&quot; |
| COMPLETED | &quot;completed&quot; |



