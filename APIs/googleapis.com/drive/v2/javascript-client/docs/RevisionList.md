# GoogleDriveApi.RevisionList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | The ETag of the list. | [optional] 
**items** | [**[Revision]**](Revision.md) | The list of revisions. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 
**kind** | **String** | This is always &#x60;drive#revisionList&#x60;. | [optional] [default to &#39;drive#revisionList&#39;]
**nextPageToken** | **String** | The page token for the next page of revisions. This field will be absent if the end of the revisions list has been reached. If the token is rejected for any reason, it should be discarded and pagination should be restarted from the first page of results. | [optional] 
**selfLink** | **String** | A link back to this list. | [optional] 


