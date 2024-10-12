# GoogleDriveApi.CommentReply

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User**](User.md) |  | [optional] 
**content** | **String** | The plain text content used to create this reply. This is not HTML safe and should only be used as a starting point to make edits to a reply&#39;s content. This field is required on inserts if no verb is specified (resolve/reopen). | [optional] 
**createdDate** | **Date** | The date when this reply was first created. | [optional] 
**deleted** | **Boolean** | Output only. Whether this reply has been deleted. If a reply has been deleted the content will be cleared and this will only represent a reply that once existed. | [optional] 
**htmlContent** | **String** | Output only. HTML formatted content for this reply. | [optional] 
**kind** | **String** | Output only. This is always &#x60;drive#commentReply&#x60;. | [optional] [default to &#39;drive#commentReply&#39;]
**modifiedDate** | **Date** | The date when this reply was last modified. | [optional] 
**replyId** | **String** | Output only. The ID of the reply. | [optional] 
**verb** | **String** | The action this reply performed to the parent comment. When creating a new reply this is the action to be perform to the parent comment. Possible values are: * &#x60;resolve&#x60; - To resolve a comment. * &#x60;reopen&#x60; - To reopen (un-resolve) a comment. | [optional] 


