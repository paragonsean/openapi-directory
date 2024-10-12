# YouTubeDataApiV3.CommentSnippet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorChannelId** | [**CommentSnippetAuthorChannelId**](CommentSnippetAuthorChannelId.md) |  | [optional] 
**authorChannelUrl** | **String** | Link to the author&#39;s YouTube channel, if any. | [optional] 
**authorDisplayName** | **String** | The name of the user who posted the comment. | [optional] 
**authorProfileImageUrl** | **String** | The URL for the avatar of the user who posted the comment. | [optional] 
**canRate** | **Boolean** | Whether the current viewer can rate this comment. | [optional] 
**channelId** | **String** | The id of the corresponding YouTube channel. In case of a channel comment this is the channel the comment refers to. In case of a video comment it&#39;s the video&#39;s channel. | [optional] 
**likeCount** | **Number** | The total number of likes this comment has received. | [optional] 
**moderationStatus** | **String** | The comment&#39;s moderation status. Will not be set if the comments were requested through the id filter. | [optional] 
**parentId** | **String** | The unique id of the parent comment, only set for replies. | [optional] 
**publishedAt** | **Date** | The date and time when the comment was originally published. | [optional] 
**textDisplay** | **String** | The comment&#39;s text. The format is either plain text or HTML dependent on what has been requested. Even the plain text representation may differ from the text originally posted in that it may replace video links with video titles etc. | [optional] 
**textOriginal** | **String** | The comment&#39;s original raw text as initially posted or last updated. The original text will only be returned if it is accessible to the viewer, which is only guaranteed if the viewer is the comment&#39;s author. | [optional] 
**updatedAt** | **Date** | The date and time when the comment was last updated. | [optional] 
**videoId** | **String** | The ID of the video the comment refers to, if any. | [optional] 
**viewerRating** | **String** | The rating the viewer has given to this comment. For the time being this will never return RATE_TYPE_DISLIKE and instead return RATE_TYPE_NONE. This may change in the future. | [optional] 



## Enum: ModerationStatusEnum


* `published` (value: `"published"`)

* `heldForReview` (value: `"heldForReview"`)

* `likelySpam` (value: `"likelySpam"`)

* `rejected` (value: `"rejected"`)





## Enum: ViewerRatingEnum


* `none` (value: `"none"`)

* `like` (value: `"like"`)

* `dislike` (value: `"dislike"`)




