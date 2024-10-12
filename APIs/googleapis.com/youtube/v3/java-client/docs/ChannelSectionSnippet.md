

# ChannelSectionSnippet

Basic details about a channel section, including title, style and position.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | The ID that YouTube uses to uniquely identify the channel that published the channel section. |  [optional] |
|**defaultLanguage** | **String** | The language of the channel section&#39;s default title and description. |  [optional] |
|**localized** | [**ChannelSectionLocalization**](ChannelSectionLocalization.md) |  |  [optional] |
|**position** | **Integer** | The position of the channel section in the channel. |  [optional] |
|**style** | [**StyleEnum**](#StyleEnum) | The style of the channel section. |  [optional] |
|**title** | **String** | The channel section&#39;s title for multiple_playlists and multiple_channels. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the channel section. |  [optional] |



## Enum: StyleEnum

| Name | Value |
|---- | -----|
| CHANNELSECTION_STYLE_UNSPECIFIED | &quot;channelsectionStyleUnspecified&quot; |
| HORIZONTAL_ROW | &quot;horizontalRow&quot; |
| VERTICAL_LIST | &quot;verticalList&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHANNELSECTION_TYPE_UNDEFINED | &quot;channelsectionTypeUndefined&quot; |
| SINGLE_PLAYLIST | &quot;singlePlaylist&quot; |
| MULTIPLE_PLAYLISTS | &quot;multiplePlaylists&quot; |
| POPULAR_UPLOADS | &quot;popularUploads&quot; |
| RECENT_UPLOADS | &quot;recentUploads&quot; |
| LIKES | &quot;likes&quot; |
| ALL_PLAYLISTS | &quot;allPlaylists&quot; |
| LIKED_PLAYLISTS | &quot;likedPlaylists&quot; |
| RECENT_POSTS | &quot;recentPosts&quot; |
| RECENT_ACTIVITY | &quot;recentActivity&quot; |
| LIVE_EVENTS | &quot;liveEvents&quot; |
| UPCOMING_EVENTS | &quot;upcomingEvents&quot; |
| COMPLETED_EVENTS | &quot;completedEvents&quot; |
| MULTIPLE_CHANNELS | &quot;multipleChannels&quot; |
| POSTED_VIDEOS | &quot;postedVideos&quot; |
| POSTED_PLAYLISTS | &quot;postedPlaylists&quot; |
| SUBSCRIPTIONS | &quot;subscriptions&quot; |



