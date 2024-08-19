

# Query

Defines a search query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayText** | **String** | The display version of the query term. This version of the query term may contain special characters that highlight the search term found in the query string. The string contains the highlighting characters only if the query enabled hit highlighting |  [optional] [readonly] |
|**searchLink** | **String** |  |  [optional] [readonly] |
|**text** | **String** | The query string. Use this string as the query term in a new search request. |  |
|**thumbnail** | [**ImageObject**](ImageObject.md) |  |  [optional] |
|**webSearchUrl** | **String** | The URL that takes the user to the Bing search results page for the query.Only related search results include this field. |  [optional] [readonly] |



