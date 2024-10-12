

# CommentThreadSnippet

Basic details about a comment thread.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canReply** | **Boolean** | Whether the current viewer of the thread can reply to it. This is viewer specific - other viewers may see a different value for this field. |  [optional] |
|**channelId** | **String** | The YouTube channel the comments in the thread refer to or the channel with the video the comments refer to. If video_id isn&#39;t set the comments refer to the channel itself. |  [optional] |
|**isPublic** | **Boolean** | Whether the thread (and therefore all its comments) is visible to all YouTube users. |  [optional] |
|**topLevelComment** | [**Comment**](Comment.md) |  |  [optional] |
|**totalReplyCount** | **Integer** | The total number of replies (not including the top level comment). |  [optional] |
|**videoId** | **String** | The ID of the video the comments refer to, if any. No video_id implies a channel discussion comment. |  [optional] |



