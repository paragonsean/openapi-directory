# AwsResourceAccessManager.ListPermissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceType** | **String** | &lt;p&gt;Specifies that you want to list only those permissions that apply to the specified resource type. This parameter is not case sensitive.&lt;/p&gt; &lt;p&gt;For example, to list only permissions that apply to Amazon EC2 subnets, specify &lt;code&gt;ec2:subnet&lt;/code&gt;. You can use the &lt;a&gt;ListResourceTypes&lt;/a&gt; operation to get the specific string required.&lt;/p&gt; | [optional] 
**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 
**maxResults** | **Number** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. | [optional] 
**permissionType** | **String** | &lt;p&gt;Specifies that you want to list only permissions of this type:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;AWS&lt;/code&gt; – returns only Amazon Web Services managed permissions.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LOCAL&lt;/code&gt; – returns only customer managed permissions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – returns both Amazon Web Services managed permissions and customer managed permissions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t specify this parameter, the default is &lt;code&gt;All&lt;/code&gt;.&lt;/p&gt; | [optional] 



## Enum: PermissionTypeEnum


* `ALL` (value: `"ALL"`)

* `AWS_MANAGED` (value: `"AWS_MANAGED"`)

* `CUSTOMER_MANAGED` (value: `"CUSTOMER_MANAGED"`)




