# GoogleDriveApi.CommentReplyList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**[CommentReply]**](CommentReply.md) | The list of replies. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 
**kind** | **String** | This is always &#x60;drive#commentReplyList&#x60;. | [optional] [default to &#39;drive#commentReplyList&#39;]
**nextLink** | **String** | A link to the next page of replies. | [optional] 
**nextPageToken** | **String** | The page token for the next page of replies. This will be absent if the end of the replies list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. | [optional] 
**selfLink** | **String** | A link back to this list. | [optional] 


