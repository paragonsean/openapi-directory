

# VideoSnippet

Basic details about a video, including title, description, uploader, thumbnails and category.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryId** | **String** | The YouTube video category associated with the video. |  [optional] |
|**channelId** | **String** | The ID that YouTube uses to uniquely identify the channel that the video was uploaded to. |  [optional] |
|**channelTitle** | **String** | Channel title for the channel that the video belongs to. |  [optional] |
|**defaultAudioLanguage** | **String** | The default_audio_language property specifies the language spoken in the video&#39;s default audio track. |  [optional] |
|**defaultLanguage** | **String** | The language of the videos&#39;s default snippet. |  [optional] |
|**description** | **String** | The video&#39;s description. @mutable youtube.videos.insert youtube.videos.update |  [optional] |
|**liveBroadcastContent** | [**LiveBroadcastContentEnum**](#LiveBroadcastContentEnum) | Indicates if the video is an upcoming/active live broadcast. Or it&#39;s \&quot;none\&quot; if the video is not an upcoming/active live broadcast. |  [optional] |
|**localized** | [**VideoLocalization**](VideoLocalization.md) |  |  [optional] |
|**publishedAt** | **OffsetDateTime** | The date and time when the video was uploaded. |  [optional] |
|**tags** | **List&lt;String&gt;** | A list of keyword tags associated with the video. Tags may contain spaces. |  [optional] |
|**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  |  [optional] |
|**title** | **String** | The video&#39;s title. @mutable youtube.videos.insert youtube.videos.update |  [optional] |



## Enum: LiveBroadcastContentEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| UPCOMING | &quot;upcoming&quot; |
| LIVE | &quot;live&quot; |
| COMPLETED | &quot;completed&quot; |



