

# Query

Defines a search query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayText** | **String** | The display version of the query term. This version of the query term may contain special characters that highlight the search term found in the query string. The string contains the highlighting characters only if the query enabled hit highlighting |  [optional] [readonly] |
|**searchLink** | **String** | The URL that you use to get the results of the related search. Before using the URL, you must append query parameters as appropriate and include the Ocp-Apim-Subscription-Key header. Use this URL if you&#39;re displaying the results in your own user interface. Otherwise, use the webSearchUrl URL. |  [optional] [readonly] |
|**text** | **String** | The query string. Use this string as the query term in a new search request. |  |
|**thumbnail** | [**ImageObject**](ImageObject.md) |  |  [optional] |
|**webSearchUrl** | **String** | The URL that takes the user to the Bing search results page for the query.Only related search results include this field. |  [optional] [readonly] |



