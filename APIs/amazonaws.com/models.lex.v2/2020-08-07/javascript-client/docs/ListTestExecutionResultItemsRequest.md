# AmazonLexModelBuildingV2.ListTestExecutionResultItemsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resultFilterBy** | [**ListTestExecutionResultItemsRequestResultFilterBy**](ListTestExecutionResultItemsRequestResultFilterBy.md) |  | 
**maxResults** | **Number** | The maximum number of test execution result items to return in each page. If there are fewer results than the max page size, only the actual number of results are returned. | [optional] 
**nextToken** | **String** | If the response from the &lt;code&gt;ListTestExecutionResultItems&lt;/code&gt; operation contains more results than specified in the &lt;code&gt;maxResults&lt;/code&gt; parameter, a token is returned in the response. Use that token in the &lt;code&gt;nextToken&lt;/code&gt; parameter to return the next page of results. | [optional] 


