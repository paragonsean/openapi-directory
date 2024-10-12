# GoogleDriveApi.FileList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **String** | The ETag of the list. | [optional] 
**incompleteSearch** | **Boolean** | Whether the search process was incomplete. If true, then some search results may be missing, since all documents were not searched. This may occur when searching multiple drives with the \&quot;allDrives\&quot; corpora, but all corpora could not be searched. When this happens, it is suggested that clients narrow their query by choosing a different corpus such as \&quot;default\&quot; or \&quot;drive\&quot;. | [optional] 
**items** | **[File]** | The list of files. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 
**kind** | **String** | This is always &#x60;drive#fileList&#x60;. | [optional] [default to &#39;drive#fileList&#39;]
**nextLink** | **String** | A link to the next page of files. | [optional] 
**nextPageToken** | **String** | The page token for the next page of files. This will be absent if the end of the files list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. | [optional] 
**selfLink** | **String** | A link back to this list. | [optional] 


