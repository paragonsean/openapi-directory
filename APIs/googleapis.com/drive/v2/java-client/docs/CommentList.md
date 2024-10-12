

# CommentList

A list of comments on a file in Google Drive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;Comment&gt;**](Comment.md) | The list of comments. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. |  [optional] |
|**kind** | **String** | This is always &#x60;drive#commentList&#x60;. |  [optional] |
|**nextLink** | **String** | A link to the next page of comments. |  [optional] |
|**nextPageToken** | **String** | The page token for the next page of comments. This will be absent if the end of the comments list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. |  [optional] |
|**selfLink** | **String** | A link back to this list. |  [optional] |



