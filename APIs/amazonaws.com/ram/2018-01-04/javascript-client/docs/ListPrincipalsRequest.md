# AwsResourceAccessManager.ListPrincipalsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceOwner** | **String** | &lt;p&gt;Specifies that you want to list information for only resource shares that match the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;SELF&lt;/code&gt; &lt;/b&gt; – principals that your account is sharing resources with&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt; &lt;code&gt;OTHER-ACCOUNTS&lt;/code&gt; &lt;/b&gt; – principals that are sharing resources with your account&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**resourceArn** | **String** | Specifies that you want to list principal information for the resource share with the specified &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt;. | [optional] 
**principals** | **[String]** | &lt;p&gt;Specifies that you want to list information for only the listed principals.&lt;/p&gt; &lt;p&gt;You can include the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An Amazon Web Services account ID, for example: &lt;code&gt;123456789012&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of an organization in Organizations, for example: &lt;code&gt;organizations::123456789012:organization/o-exampleorgid&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An ARN of an organizational unit (OU) in Organizations, for example: &lt;code&gt;organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An ARN of an IAM role, for example: &lt;code&gt;iam::123456789012:role/rolename&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An ARN of an IAM user, for example: &lt;code&gt;iam::123456789012user/username&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;Not all resource types can be shared with IAM roles and users. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types\&quot;&gt;Sharing with IAM roles and users&lt;/a&gt; in the &lt;i&gt;Resource Access Manager User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; | [optional] 
**resourceType** | **String** | &lt;p&gt;Specifies that you want to list information for only principals associated with resource shares that include the specified resource type.&lt;/p&gt; &lt;p&gt;For a list of valid values, query the &lt;a&gt;ListResourceTypes&lt;/a&gt; operation.&lt;/p&gt; | [optional] 
**resourceShareArns** | **[String]** | Specifies that you want to list information for only principals associated with the resource shares specified by a list the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Names (ARNs)&lt;/a&gt;. | [optional] 
**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 
**maxResults** | **Number** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. | [optional] 



## Enum: ResourceOwnerEnum


* `SELF` (value: `"SELF"`)

* `OTHER-ACCOUNTS` (value: `"OTHER-ACCOUNTS"`)




