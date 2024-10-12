

# ListResourcesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceOwner** | [**ResourceOwnerEnum**](#ResourceOwnerEnum) | &lt;p&gt;Specifies that you want to list only the resource shares that match the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;SELF&lt;/code&gt; &lt;/b&gt; – resources that your account shares with other accounts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;OTHER-ACCOUNTS&lt;/code&gt; &lt;/b&gt; – resources that other accounts share with your account&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**principal** | **String** | Specifies that you want to list only the resource shares that are associated with the specified principal. |  [optional] |
|**resourceType** | **String** | &lt;p&gt;Specifies that you want to list only the resource shares that include resources of the specified resource type.&lt;/p&gt; &lt;p&gt;For valid values, query the &lt;a&gt;ListResourceTypes&lt;/a&gt; operation.&lt;/p&gt; |  [optional] |
|**resourceArns** | **List&lt;String&gt;** | Specifies that you want to list only the resource shares that include resources with the specified &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt;. |  [optional] |
|**resourceShareArns** | **List&lt;String&gt;** | Specifies that you want to list only resources in the resource shares identified by the specified &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt;. |  [optional] |
|**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. |  [optional] |
|**maxResults** | **Integer** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. |  [optional] |
|**resourceRegionScope** | [**ResourceRegionScopeEnum**](#ResourceRegionScopeEnum) | &lt;p&gt;Specifies that you want the results to include only resources that have the specified scope.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – the results include both global and regional resources or resource types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;GLOBAL&lt;/code&gt; – the results include only global resources or resource types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;REGIONAL&lt;/code&gt; – the results include only regional resources or resource types.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The default value is &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; |  [optional] |



## Enum: ResourceOwnerEnum

| Name | Value |
|---- | -----|
| SELF | &quot;SELF&quot; |
| OTHER_ACCOUNTS | &quot;OTHER-ACCOUNTS&quot; |



## Enum: ResourceRegionScopeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;ALL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |
| GLOBAL | &quot;GLOBAL&quot; |



