# GoogleDriveApi.FileList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **[File]** | The list of files. If nextPageToken is populated, then this list may be incomplete and an additional page of results should be fetched. | [optional] 
**incompleteSearch** | **Boolean** | Whether the search process was incomplete. If true, then some search results might be missing, since all documents were not searched. This can occur when searching multiple drives with the &#39;allDrives&#39; corpora, but all corpora couldn&#39;t be searched. When this happens, it&#39;s suggested that clients narrow their query by choosing a different corpus such as &#39;user&#39; or &#39;drive&#39;. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#fileList\&quot;&#x60;. | [optional] [default to &#39;drive#fileList&#39;]
**nextPageToken** | **String** | The page token for the next page of files. This will be absent if the end of the files list has been reached. If the token is rejected for any reason, it should be discarded, and pagination should be restarted from the first page of results. The page token is typically valid for several hours. However, if new items are added or removed, your expected results might differ. | [optional] 


