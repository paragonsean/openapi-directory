# GoogleDriveApi.Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **String** | A region of the document represented as a JSON string. For details on defining anchor properties, refer to [Add comments and replies](https://developers.google.com/drive/api/v2/manage-comments). | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**commentId** | **String** | Output only. The ID of the comment. | [optional] 
**content** | **String** | The plain text content used to create this comment. This is not HTML safe and should only be used as a starting point to make edits to a comment&#39;s content. | [optional] 
**context** | [**CommentContext**](CommentContext.md) |  | [optional] 
**createdDate** | **Date** | The date when this comment was first created. | [optional] 
**deleted** | **Boolean** | Output only. Whether this comment has been deleted. If a comment has been deleted the content will be cleared and this will only represent a comment that once existed. | [optional] 
**fileId** | **String** | Output only. The file which this comment is addressing. | [optional] 
**fileTitle** | **String** | Output only. The title of the file which this comment is addressing. | [optional] 
**htmlContent** | **String** | Output only. HTML formatted content for this comment. | [optional] 
**kind** | **String** | Output only. This is always &#x60;drive#comment&#x60;. | [optional] [default to &#39;drive#comment&#39;]
**modifiedDate** | **Date** | The date when this comment or any of its replies were last modified. | [optional] 
**replies** | [**[CommentReply]**](CommentReply.md) | Output only. Replies to this post. | [optional] 
**selfLink** | **String** | Output only. A link back to this comment. | [optional] 
**status** | **String** | Output only. The status of this comment. Status can be changed by posting a reply to a comment with the desired status. * &#x60;open&#x60; - The comment is still open. * &#x60;resolved&#x60; - The comment has been resolved by one of its replies. | [optional] 


