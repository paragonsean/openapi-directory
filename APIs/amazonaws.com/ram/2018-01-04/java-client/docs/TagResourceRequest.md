

# TagResourceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceShareArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share that you want to add tags to. You must specify &lt;i&gt;either&lt;/i&gt; &lt;code&gt;resourceShareArn&lt;/code&gt;, or &lt;code&gt;resourceArn&lt;/code&gt;, but not both. |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A list of one or more tag key and value pairs. The tag key must be present and not be an empty string. The tag value must be present but can be an empty string. |  |
|**resourceArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the managed permission that you want to add tags to. You must specify &lt;i&gt;either&lt;/i&gt; &lt;code&gt;resourceArn&lt;/code&gt;, or &lt;code&gt;resourceShareArn&lt;/code&gt;, but not both. |  [optional] |



