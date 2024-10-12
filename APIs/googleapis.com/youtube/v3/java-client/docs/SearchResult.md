

# SearchResult

A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | Etag of this resource. |  [optional] |
|**id** | [**ResourceId**](ResourceId.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;youtube#searchResult\&quot;. |  [optional] |
|**snippet** | [**SearchResultSnippet**](SearchResultSnippet.md) |  |  [optional] |



