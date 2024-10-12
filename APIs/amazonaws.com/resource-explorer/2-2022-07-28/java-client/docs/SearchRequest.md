

# SearchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxResults** | **Integer** | &lt;p&gt;The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the &lt;code&gt;NextToken&lt;/code&gt; response element is present and has a value (is not null). Include that value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results.&lt;/p&gt; &lt;note&gt; &lt;p&gt;An API operation can return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**nextToken** | **String** | The parameter for receiving additional results if you receive a &lt;code&gt;NextToken&lt;/code&gt; response in a previous request. A &lt;code&gt;NextToken&lt;/code&gt; response indicates that more output is available. Set this parameter to the value of the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to indicate where the output should continue from. |  [optional] |
|**queryString** | **String** | &lt;p&gt;A string that includes keywords and filters that specify the resources that you want to include in the results.&lt;/p&gt; &lt;p&gt;For the complete syntax supported by the &lt;code&gt;QueryString&lt;/code&gt; parameter, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html\&quot;&gt;Search query syntax reference for Resource Explorer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The search is completely case insensitive. You can specify an empty string to return all results up to the limit of 1,000 total results.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The operation can return only the first 1,000 results. If the resource you want is not included, then use a different value for &lt;code&gt;QueryString&lt;/code&gt; to refine the results.&lt;/p&gt; &lt;/note&gt; |  |
|**viewArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon resource name (ARN)&lt;/a&gt; of the view to use for the query. If you don&#39;t specify a value for this parameter, then the operation automatically uses the default view for the Amazon Web Services Region in which you called this operation. If the Region either doesn&#39;t have a default view or if you don&#39;t have permission to use the default view, then the operation fails with a &lt;code&gt;401 Unauthorized&lt;/code&gt; exception. |  [optional] |



