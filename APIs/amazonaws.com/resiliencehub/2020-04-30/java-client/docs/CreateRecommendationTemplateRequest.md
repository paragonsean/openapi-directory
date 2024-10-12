

# CreateRecommendationTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assessmentArn** | **String** | Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app-assessment/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  |
|**bucketName** | **String** | The name of the Amazon S3 bucket that will contain the recommendation template. |  [optional] |
|**clientToken** | **String** | Used for an idempotency token. A client token is a unique, case-sensitive string of up to 64 ASCII characters. You should not reuse the same client token for other API requests. |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | &lt;p&gt;The format for the recommendation template.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;CfnJson&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The template is CloudFormation JSON.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;CfnYaml&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The template is CloudFormation YAML.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; |  [optional] |
|**name** | **String** | The name for the recommendation template. |  |
|**recommendationIds** | **List&lt;String&gt;** | Identifiers for the recommendations used to create a recommendation template. |  [optional] |
|**recommendationTypes** | **List&lt;RenderRecommendationType&gt;** | &lt;p&gt;An array of strings that specify the recommendation template type or types.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;Alarm&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The template is an &lt;a&gt;AlarmRecommendation&lt;/a&gt; template.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Sop&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The template is a &lt;a&gt;SopRecommendation&lt;/a&gt; template.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Test&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The template is a &lt;a&gt;TestRecommendation&lt;/a&gt; template.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CFN_YAML | &quot;CfnYaml&quot; |
| CFN_JSON | &quot;CfnJson&quot; |



