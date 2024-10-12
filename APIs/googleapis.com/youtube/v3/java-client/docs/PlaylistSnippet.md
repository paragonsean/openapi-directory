

# PlaylistSnippet

Basic details about a playlist, including title, description and thumbnails.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | The ID that YouTube uses to uniquely identify the channel that published the playlist. |  [optional] |
|**channelTitle** | **String** | The channel title of the channel that the video belongs to. |  [optional] |
|**defaultLanguage** | **String** | The language of the playlist&#39;s default title and description. |  [optional] |
|**description** | **String** | The playlist&#39;s description. |  [optional] |
|**localized** | [**PlaylistLocalization**](PlaylistLocalization.md) |  |  [optional] |
|**publishedAt** | **OffsetDateTime** | The date and time that the playlist was created. |  [optional] |
|**tags** | **List&lt;String&gt;** | Keyword tags associated with the playlist. |  [optional] |
|**thumbnailVideoId** | **String** | Note: if the playlist has a custom thumbnail, this field will not be populated. The video id selected by the user that will be used as the thumbnail of this playlist. This field defaults to the first publicly viewable video in the playlist, if: 1. The user has never selected a video to be the thumbnail of the playlist. 2. The user selects a video to be the thumbnail, and then removes that video from the playlist. 3. The user selects a non-owned video to be the thumbnail, but that video becomes private, or gets deleted. |  [optional] |
|**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  |  [optional] |
|**title** | **String** | The playlist&#39;s title. |  [optional] |



