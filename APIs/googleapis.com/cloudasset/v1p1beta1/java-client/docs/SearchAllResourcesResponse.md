

# SearchAllResourcesResponse

Search all resources response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | If there are more results than those appearing in this response, then &#x60;next_page_token&#x60; is included. To get the next set of results, call this method again using the value of &#x60;next_page_token&#x60; as &#x60;page_token&#x60;. |  [optional] |
|**results** | [**List&lt;StandardResourceMetadata&gt;**](StandardResourceMetadata.md) | A list of resource that match the search query. |  [optional] |



