

# ListViewsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxResults** | **Integer** | &lt;p&gt;The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the &lt;code&gt;NextToken&lt;/code&gt; response element is present and has a value (is not null). Include that value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results.&lt;/p&gt; &lt;note&gt; &lt;p&gt;An API operation can return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**nextToken** | **String** | The parameter for receiving additional results if you receive a &lt;code&gt;NextToken&lt;/code&gt; response in a previous request. A &lt;code&gt;NextToken&lt;/code&gt; response indicates that more output is available. Set this parameter to the value of the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to indicate where the output should continue from. |  [optional] |



