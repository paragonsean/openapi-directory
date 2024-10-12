# GoogleApi.Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**CommentActor**](CommentActor.md) |  | [optional] 
**etag** | **String** | ETag of this response for caching purposes. | [optional] 
**id** | **String** | The ID of this comment. | [optional] 
**inReplyTo** | [**[CommentInReplyToInner]**](CommentInReplyToInner.md) | The activity this comment replied to. | [optional] 
**kind** | **String** | Identifies this resource as a comment. Value: \&quot;plus#comment\&quot;. | [optional] [default to &#39;plus#comment&#39;]
**object** | [**CommentObject**](CommentObject.md) |  | [optional] 
**plusoners** | [**CommentPlusoners**](CommentPlusoners.md) |  | [optional] 
**published** | **Date** | The time at which this comment was initially published. Formatted as an RFC 3339 timestamp. | [optional] 
**selfLink** | **String** | Link to this comment resource. | [optional] 
**updated** | **Date** | The time at which this comment was last updated. Formatted as an RFC 3339 timestamp. | [optional] 
**verb** | **String** | This comment&#39;s verb, indicating what action was performed. Possible values are:   - \&quot;post\&quot; - Publish content to the stream. | [optional] [default to &#39;post&#39;]


