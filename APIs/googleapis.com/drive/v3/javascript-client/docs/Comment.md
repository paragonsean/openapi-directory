# GoogleDriveApi.Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anchor** | **String** | A region of the document represented as a JSON string. For details on defining anchor properties, refer to [Manage comments and replies](https://developers.google.com/drive/api/v3/manage-comments). | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**content** | **String** | The plain text content of the comment. This field is used for setting the content, while &#x60;htmlContent&#x60; should be displayed. | [optional] 
**createdTime** | **Date** | The time at which the comment was created (RFC 3339 date-time). | [optional] 
**deleted** | **Boolean** | Output only. Whether the comment has been deleted. A deleted comment has no content. | [optional] 
**htmlContent** | **String** | Output only. The content of the comment with HTML formatting. | [optional] 
**id** | **String** | Output only. The ID of the comment. | [optional] 
**kind** | **String** | Output only. Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#comment\&quot;&#x60;. | [optional] [default to &#39;drive#comment&#39;]
**modifiedTime** | **Date** | The last time the comment or any of its replies was modified (RFC 3339 date-time). | [optional] 
**quotedFileContent** | [**CommentQuotedFileContent**](CommentQuotedFileContent.md) |  | [optional] 
**replies** | [**[Reply]**](Reply.md) | Output only. The full list of replies to the comment in chronological order. | [optional] 
**resolved** | **Boolean** | Output only. Whether the comment has been resolved by one of its replies. | [optional] 


