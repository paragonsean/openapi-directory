# YouTubeDataApiV3.ActivitySnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelId** | **String** | The ID that YouTube uses to uniquely identify the channel associated with the activity. | [optional] 
**channelTitle** | **String** | Channel title for the channel responsible for this activity | [optional] 
**description** | **String** | The description of the resource primarily associated with the activity. @mutable youtube.activities.insert | [optional] 
**groupId** | **String** | The group ID associated with the activity. A group ID identifies user events that are associated with the same user and resource. For example, if a user rates a video and marks the same video as a favorite, the entries for those events would have the same group ID in the user&#39;s activity feed. In your user interface, you can avoid repetition by grouping events with the same groupId value. | [optional] 
**publishedAt** | **Date** | The date and time that the video was uploaded. | [optional] 
**thumbnails** | [**ThumbnailDetails**](ThumbnailDetails.md) |  | [optional] 
**title** | **String** | The title of the resource primarily associated with the activity. | [optional] 
**type** | **String** | The type of activity that the resource describes. | [optional] 



## Enum: TypeEnum


* `typeUnspecified` (value: `"typeUnspecified"`)

* `upload` (value: `"upload"`)

* `like` (value: `"like"`)

* `favorite` (value: `"favorite"`)

* `comment` (value: `"comment"`)

* `subscription` (value: `"subscription"`)

* `playlistItem` (value: `"playlistItem"`)

* `recommendation` (value: `"recommendation"`)

* `bulletin` (value: `"bulletin"`)

* `social` (value: `"social"`)

* `channelItem` (value: `"channelItem"`)

* `promotedItem` (value: `"promotedItem"`)




