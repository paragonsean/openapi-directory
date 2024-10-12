# CloudSearchApi.SearchResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusteredResults** | [**[SearchResult]**](SearchResult.md) | If source is clustered, provide list of clustered results. There will only be one level of clustered results. If current source is not enabled for clustering, this field will be empty. | [optional] 
**debugInfo** | [**ResultDebugInfo**](ResultDebugInfo.md) |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**snippet** | [**Snippet**](Snippet.md) |  | [optional] 
**title** | **String** | Title of the search result. | [optional] 
**url** | **String** | The URL of the search result. The URL contains a Google redirect to the actual item. This URL is signed and shouldn&#39;t be changed. | [optional] 


