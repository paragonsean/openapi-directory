# AwsResourceAccessManager.ListPermissionAssociationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissionArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the managed permission. | [optional] 
**permissionVersion** | **Number** | Specifies that you want to list only those associations with resource shares that use this version of the managed permission. If you don&#39;t provide a value for this parameter, then the operation returns information about associations with resource shares that use any version of the managed permission. | [optional] 
**associationStatus** | **String** | Specifies that you want to list only those associations with resource shares that match this status. | [optional] 
**resourceType** | **String** | Specifies that you want to list only those associations with resource shares that include at least one resource of this resource type. | [optional] 
**featureSet** | **String** | Specifies that you want to list only those associations with resource shares that have a &lt;code&gt;featureSet&lt;/code&gt; with this value. | [optional] 
**defaultVersion** | **Boolean** | &lt;p&gt;When &lt;code&gt;true&lt;/code&gt;, specifies that you want to list only those associations with resource shares that use the default version of the specified managed permission.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;false&lt;/code&gt; (the default value), lists associations with resource shares that use any version of the specified managed permission.&lt;/p&gt; | [optional] 
**nextToken** | **String** | Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 
**maxResults** | **Number** | Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the &lt;code&gt;NextToken&lt;/code&gt; response element is returned with a value (not null). Include the specified value as the &lt;code&gt;NextToken&lt;/code&gt; request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check &lt;code&gt;NextToken&lt;/code&gt; after every operation to ensure that you receive all of the results. | [optional] 



## Enum: AssociationStatusEnum


* `ASSOCIATING` (value: `"ASSOCIATING"`)

* `ASSOCIATED` (value: `"ASSOCIATED"`)

* `FAILED` (value: `"FAILED"`)

* `DISASSOCIATING` (value: `"DISASSOCIATING"`)

* `DISASSOCIATED` (value: `"DISASSOCIATED"`)





## Enum: FeatureSetEnum


* `CREATED_FROM_POLICY` (value: `"CREATED_FROM_POLICY"`)

* `PROMOTING_TO_STANDARD` (value: `"PROMOTING_TO_STANDARD"`)

* `STANDARD` (value: `"STANDARD"`)




