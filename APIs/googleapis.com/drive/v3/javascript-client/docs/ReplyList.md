# GoogleDriveApi.ReplyList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#replyList\&quot;&#x60;. | [optional] [default to &#39;drive#replyList&#39;]
**nextPageToken** | **String** | The page token for the next page of replies. This will be absent if the end of the replies list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. The page token is typically valid for several hours. However, if new items are added or removed, your expected results might differ. | [optional] 
**replies** | [**[Reply]**](Reply.md) | The list of replies. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 


