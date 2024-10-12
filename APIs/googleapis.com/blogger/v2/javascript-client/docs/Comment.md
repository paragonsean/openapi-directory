# BloggerApi.Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommentAuthor**](CommentAuthor.md) |  | [optional] 
**blog** | [**CommentBlog**](CommentBlog.md) |  | [optional] 
**content** | **String** | The actual content of the comment. May include HTML markup. | [optional] 
**id** | **String** | The identifier for this resource. | [optional] 
**inReplyTo** | [**CommentInReplyTo**](CommentInReplyTo.md) |  | [optional] 
**kind** | **String** | The kind of this entry. Always blogger#comment. | [optional] 
**post** | [**CommentPost**](CommentPost.md) |  | [optional] 
**published** | **String** | RFC 3339 date-time when this comment was published. | [optional] 
**selfLink** | **String** | The API REST URL to fetch this resource from. | [optional] 
**status** | **String** | The status of the comment (only populated for admin users). | [optional] 
**updated** | **String** | RFC 3339 date-time when this comment was last updated. | [optional] 



## Enum: StatusEnum


* `LIVE` (value: `"LIVE"`)

* `EMPTIED` (value: `"EMPTIED"`)

* `PENDING` (value: `"PENDING"`)

* `SPAM` (value: `"SPAM"`)




