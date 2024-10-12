# AwsResilienceHub.DeleteAppVersionResourceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | 
**awsAccountId** | **String** | Amazon Web Services account that owns the physical resource. | [optional] 
**awsRegion** | **String** | Amazon Web Services region that owns the physical resource. | [optional] 
**clientToken** | **String** | Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests. | [optional] 
**logicalResourceId** | [**CreateAppVersionResourceRequestLogicalResourceId**](CreateAppVersionResourceRequestLogicalResourceId.md) |  | [optional] 
**physicalResourceId** | **String** | Physical identifier of the resource. | [optional] 
**resourceName** | **String** | Name of the resource. | [optional] 


