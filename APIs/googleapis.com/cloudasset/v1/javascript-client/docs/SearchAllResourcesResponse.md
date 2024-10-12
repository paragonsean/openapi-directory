# CloudAssetApi.SearchAllResourcesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | If there are more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. | [optional] 
**results** | [**[ResourceSearchResult]**](ResourceSearchResult.md) | A list of Resources that match the search query. It contains the resource standard metadata information. | [optional] 


