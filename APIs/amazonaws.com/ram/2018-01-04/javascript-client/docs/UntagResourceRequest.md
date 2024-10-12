# AwsResourceAccessManager.UntagResourceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceShareArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the resource share that you want to remove tags from. The tags are removed from the resource share, not the resources in the resource share. You must specify either &lt;code&gt;resourceShareArn&lt;/code&gt;, or &lt;code&gt;resourceArn&lt;/code&gt;, but not both. | [optional] 
**tagKeys** | **[String]** | Specifies a list of one or more tag keys that you want to remove. | 
**resourceArn** | **String** | Specifies the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Amazon Resource Name (ARN)&lt;/a&gt; of the managed permission that you want to remove tags from. You must specify either &lt;code&gt;resourceArn&lt;/code&gt;, or &lt;code&gt;resourceShareArn&lt;/code&gt;, but not both. | [optional] 


