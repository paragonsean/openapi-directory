

# ListBotLocalesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sortBy** | [**ListBotLocalesRequestSortBy**](ListBotLocalesRequestSortBy.md) |  |  [optional] |
|**filters** | [**List&lt;BotLocaleFilter&gt;**](BotLocaleFilter.md) | Provides the specification for a filter used to limit the response to only those locales that match the filter specification. You can only specify one filter and one value to filter on. |  [optional] |
|**maxResults** | **Integer** | The maximum number of aliases to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned. |  [optional] |
|**nextToken** | **String** | If the response from the &lt;code&gt;ListBotLocales&lt;/code&gt; operation contains more results than specified in the &lt;code&gt;maxResults&lt;/code&gt; parameter, a token is returned in the response. Use that token as the &lt;code&gt;nextToken&lt;/code&gt; parameter to return the next page of results.  |  [optional] |



