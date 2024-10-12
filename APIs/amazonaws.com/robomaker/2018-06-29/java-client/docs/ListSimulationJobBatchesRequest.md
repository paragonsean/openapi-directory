

# ListSimulationJobBatchesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextToken** | **String** | If the previous paginated request did not return all of the remaining results, the response object&#39;s &lt;code&gt;nextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListSimulationJobBatches&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;nextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s NextToken parameter is set to null.  |  [optional] |
|**maxResults** | **Integer** | When this parameter is used, &lt;code&gt;ListSimulationJobBatches&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListSimulationJobBatches&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value.  |  [optional] |
|**filters** | [**List&lt;Filter&gt;**](Filter.md) | Optional filters to limit results. |  [optional] |



