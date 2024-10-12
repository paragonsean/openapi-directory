# AmazonLexModelBuildingV2.ListExportsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botId** | **String** | The unique identifier that Amazon Lex assigned to the bot. | [optional] 
**botVersion** | **String** | The version of the bot to list exports for.  | [optional] 
**sortBy** | [**ListExportsRequestSortBy**](ListExportsRequestSortBy.md) |  | [optional] 
**filters** | [**[ExportFilter]**](ExportFilter.md) | Provides the specification of a filter used to limit the exports in the response to only those that match the filter specification. You can only specify one filter and one string to filter on. | [optional] 
**maxResults** | **Number** | The maximum number of exports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned. | [optional] 
**nextToken** | **String** | &lt;p&gt;If the response from the &lt;code&gt;ListExports&lt;/code&gt; operation contains more results that specified in the &lt;code&gt;maxResults&lt;/code&gt; parameter, a token is returned in the response. &lt;/p&gt; &lt;p&gt;Use the returned token in the &lt;code&gt;nextToken&lt;/code&gt; parameter of a &lt;code&gt;ListExports&lt;/code&gt; request to return the next page of results. For a complete set of results, call the &lt;code&gt;ListExports&lt;/code&gt; operation until the &lt;code&gt;nextToken&lt;/code&gt; returned in the response is null.&lt;/p&gt; | [optional] 
**localeId** | **String** | Specifies the resources that should be exported. If you don&#39;t specify a resource type in the &lt;code&gt;filters&lt;/code&gt; parameter, both bot locales and custom vocabularies are exported. | [optional] 


