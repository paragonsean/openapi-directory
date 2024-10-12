# AmazonLexModelBuildingV2.ListBotsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sortBy** | [**ListBotsRequestSortBy**](ListBotsRequestSortBy.md) |  | [optional] 
**filters** | [**[BotFilter]**](BotFilter.md) | Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on. | [optional] 
**maxResults** | **Number** | The maximum number of bots to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. | [optional] 
**nextToken** | **String** | &lt;p&gt;If the response from the &lt;code&gt;ListBots&lt;/code&gt; operation contains more results than specified in the &lt;code&gt;maxResults&lt;/code&gt; parameter, a token is returned in the response. &lt;/p&gt; &lt;p&gt;Use the returned token in the &lt;code&gt;nextToken&lt;/code&gt; parameter of a &lt;code&gt;ListBots&lt;/code&gt; request to return the next page of results. For a complete set of results, call the &lt;code&gt;ListBots&lt;/code&gt; operation until the &lt;code&gt;nextToken&lt;/code&gt; returned in the response is null.&lt;/p&gt; | [optional] 


