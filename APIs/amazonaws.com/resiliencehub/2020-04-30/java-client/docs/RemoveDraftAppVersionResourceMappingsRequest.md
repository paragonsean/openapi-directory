

# RemoveDraftAppVersionResourceMappingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  |
|**appRegistryAppNames** | **List&lt;String&gt;** | The names of the registered applications you want to remove from the resource mappings. |  [optional] |
|**eksSourceNames** | **List&lt;String&gt;** | &lt;p&gt;The names of the Amazon Elastic Kubernetes Service clusters and namespaces you want to remove from the resource mappings.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This parameter accepts values in \&quot;eks-cluster/namespace\&quot; format.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**logicalStackNames** | **List&lt;String&gt;** | The names of the CloudFormation stacks you want to remove from the resource mappings. |  [optional] |
|**resourceGroupNames** | **List&lt;String&gt;** | The names of the resource groups you want to remove from the resource mappings. |  [optional] |
|**resourceNames** | **List&lt;String&gt;** | The names of the resources you want to remove from the resource mappings. |  [optional] |
|**terraformSourceNames** | **List&lt;String&gt;** | The names of the Terraform sources you want to remove from the resource mappings. |  [optional] |



