

# ImportResourcesToDraftAppVersionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  |
|**eksSources** | [**List&lt;EksSource&gt;**](EksSource.md) | The input sources of the Amazon Elastic Kubernetes Service resources you need to import. |  [optional] |
|**importStrategy** | [**ImportStrategyEnum**](#ImportStrategyEnum) | The import strategy you would like to set to import resources into Resilience Hub application. |  [optional] |
|**sourceArns** | **List&lt;String&gt;** | The Amazon Resource Names (ARNs) for the resources. |  [optional] |
|**terraformSources** | [**List&lt;TerraformSource&gt;**](TerraformSource.md) |  A list of terraform file s3 URLs you need to import.  |  [optional] |



## Enum: ImportStrategyEnum

| Name | Value |
|---- | -----|
| ADD_ONLY | &quot;AddOnly&quot; |
| REPLACE_ALL | &quot;ReplaceAll&quot; |



