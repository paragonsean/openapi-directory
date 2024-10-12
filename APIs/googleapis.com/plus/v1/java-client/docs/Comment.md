

# Comment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | [**CommentActor**](CommentActor.md) |  |  [optional] |
|**etag** | **String** | ETag of this response for caching purposes. |  [optional] |
|**id** | **String** | The ID of this comment. |  [optional] |
|**inReplyTo** | [**List&lt;CommentInReplyToInner&gt;**](CommentInReplyToInner.md) | The activity this comment replied to. |  [optional] |
|**kind** | **String** | Identifies this resource as a comment. Value: \&quot;plus#comment\&quot;. |  [optional] |
|**_object** | [**CommentObject**](CommentObject.md) |  |  [optional] |
|**plusoners** | [**CommentPlusoners**](CommentPlusoners.md) |  |  [optional] |
|**published** | **OffsetDateTime** | The time at which this comment was initially published. Formatted as an RFC 3339 timestamp. |  [optional] |
|**selfLink** | **String** | Link to this comment resource. |  [optional] |
|**updated** | **OffsetDateTime** | The time at which this comment was last updated. Formatted as an RFC 3339 timestamp. |  [optional] |
|**verb** | **String** | This comment&#39;s verb, indicating what action was performed. Possible values are:   - \&quot;post\&quot; - Publish content to the stream. |  [optional] |



