# AwsResilienceHub.UpdateAppVersionResourceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInfo** | **{String: Array}** | Currently, there is no supported additional information for resources. | [optional] 
**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | 
**appComponents** | **[String]** | List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added. | [optional] 
**awsAccountId** | **String** | Amazon Web Services account that owns the physical resource. | [optional] 
**awsRegion** | **String** | Amazon Web Services region that owns the physical resource. | [optional] 
**excluded** | **Boolean** | &lt;p&gt;Indicates if a resource is excluded from an Resilience Hub application.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can exclude only imported resources from an Resilience Hub application.&lt;/p&gt; &lt;/note&gt; | [optional] 
**logicalResourceId** | [**CreateAppVersionResourceRequestLogicalResourceId**](CreateAppVersionResourceRequestLogicalResourceId.md) |  | [optional] 
**physicalResourceId** | **String** | Physical identifier of the resource. | [optional] 
**resourceName** | **String** | Name of the resource. | [optional] 
**resourceType** | **String** | Type of resource. | [optional] 


