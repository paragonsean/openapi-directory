# AwsResourceAccessManager.ListPendingInvitationResourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceShareInvitationArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the invitation. You can use &lt;a&gt;GetResourceShareInvitations&lt;/a&gt; to find the ARN of the invitation. | 
**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 
**maxResults** | **Number** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. | [optional] 
**resourceRegionScope** | **String** | &lt;p&gt;Specifies that you want the results to include only resources that have the specified scope.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – the results include both global and regional resources or resource types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GLOBAL&lt;/code&gt; – the results include only global resources or resource types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;REGIONAL&lt;/code&gt; – the results include only regional resources or resource types.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The default value is &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; | [optional] 



## Enum: ResourceRegionScopeEnum


* `ALL` (value: `"ALL"`)

* `REGIONAL` (value: `"REGIONAL"`)

* `GLOBAL` (value: `"GLOBAL"`)




