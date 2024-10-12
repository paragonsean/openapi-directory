# AwsResourceAccessManager.GetResourceSharesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceShareArns** | **[String]** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt; of individual resource shares that you want information about. | [optional] 
**resourceShareStatus** | **String** | Specifies that you want to retrieve details of only those resource shares that have this status. | [optional] 
**resourceOwner** | **String** | &lt;p&gt;Specifies that you want to retrieve details of only those resource shares that match the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;SELF&lt;/code&gt; &lt;/b&gt; – resource shares that your account shares with other accounts&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;OTHER-ACCOUNTS&lt;/code&gt; &lt;/b&gt; – resource shares that other accounts share with your account&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**name** | **String** | Specifies the name of an individual resource share that you want to retrieve details about. | [optional] 
**tagFilters** | [**[TagFilter]**](TagFilter.md) | Specifies that you want to retrieve details of only those resource shares that match the specified tag keys and values. | [optional] 
**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 
**maxResults** | **Number** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. | [optional] 
**permissionArn** | **String** | Specifies that you want to retrieve details of only those resource shares that use the managed permission with this &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt;. | [optional] 
**permissionVersion** | **Number** | Specifies that you want to retrieve details for only those resource shares that use the specified version of the managed permission. | [optional] 



## Enum: ResourceShareStatusEnum


* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)

* `DELETED` (value: `"DELETED"`)





## Enum: ResourceOwnerEnum


* `SELF` (value: `"SELF"`)

* `OTHER-ACCOUNTS` (value: `"OTHER-ACCOUNTS"`)




