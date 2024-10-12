

# AddDraftAppVersionResourceMappingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  |
|**resourceMappings** | [**List&lt;ResourceMapping&gt;**](ResourceMapping.md) | Mappings used to map logical resources from the template to physical resources. You can use the mapping type &lt;code&gt;CFN_STACK&lt;/code&gt; if the application template uses a logical stack name. Or you can map individual resources by using the mapping type &lt;code&gt;RESOURCE&lt;/code&gt;. We recommend using the mapping type &lt;code&gt;CFN_STACK&lt;/code&gt; if the application is backed by a CloudFormation stack. |  |



