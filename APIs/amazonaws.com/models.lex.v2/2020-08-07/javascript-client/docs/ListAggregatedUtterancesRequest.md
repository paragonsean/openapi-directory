# AmazonLexModelBuildingV2.ListAggregatedUtterancesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botAliasId** | **String** | The identifier of the bot alias associated with this request. If you specify the bot alias, you can&#39;t specify the bot version. | [optional] 
**botVersion** | **String** | The identifier of the bot version associated with this request. If you specify the bot version, you can&#39;t specify the bot alias. | [optional] 
**localeId** | **String** | The identifier of the language and locale where the utterances were collected. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html\&quot;&gt;Supported languages&lt;/a&gt;. | 
**aggregationDuration** | [**ListAggregatedUtterancesRequestAggregationDuration**](ListAggregatedUtterancesRequestAggregationDuration.md) |  | 
**sortBy** | [**ListAggregatedUtterancesRequestSortBy**](ListAggregatedUtterancesRequestSortBy.md) |  | [optional] 
**filters** | [**[AggregatedUtterancesFilter]**](AggregatedUtterancesFilter.md) | Provides the specification of a filter used to limit the utterances in the response to only those that match the filter specification. You can only specify one filter and one string to filter on. | [optional] 
**maxResults** | **Number** | The maximum number of utterances to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. If you don&#39;t specify the &lt;code&gt;maxResults&lt;/code&gt; parameter, 1,000 results are returned. | [optional] 
**nextToken** | **String** | If the response from the &lt;code&gt;ListAggregatedUtterances&lt;/code&gt; operation contains more results that specified in the &lt;code&gt;maxResults&lt;/code&gt; parameter, a token is returned in the response. Use that token in the &lt;code&gt;nextToken&lt;/code&gt; parameter to return the next page of results. | [optional] 


