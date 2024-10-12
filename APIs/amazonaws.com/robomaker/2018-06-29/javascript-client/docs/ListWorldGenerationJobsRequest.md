# AwsRoboMaker.ListWorldGenerationJobsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextToken** | **String** | If the previous paginated request did not return all of the remaining results, the response object&#39;s &lt;code&gt;nextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListWorldGenerationJobsRequest&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;nextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s NextToken parameter is set to null.  | [optional] 
**maxResults** | **Number** | When this parameter is used, &lt;code&gt;ListWorldGeneratorJobs&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListWorldGeneratorJobs&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If this parameter is not used, then &lt;code&gt;ListWorldGeneratorJobs&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.  | [optional] 
**filters** | [**[Filter]**](Filter.md) | Optional filters to limit results. You can use &lt;code&gt;status&lt;/code&gt; and &lt;code&gt;templateId&lt;/code&gt;. | [optional] 


