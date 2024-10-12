# GoogleDriveApi.ChildList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | The ETag of the list. | [optional] 
**items** | [**[ChildReference]**](ChildReference.md) | The list of children. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 
**kind** | **String** | This is always &#x60;drive#childList&#x60;. | [optional] [default to &#39;drive#childList&#39;]
**nextLink** | **String** | A link to the next page of children. | [optional] 
**nextPageToken** | **String** | The page token for the next page of children. This will be absent if the end of the children list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. | [optional] 
**selfLink** | **String** | A link back to this list. | [optional] 


