# AwsResilienceHub.ListAppInputSourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. | 
**appVersion** | **String** | Resilience Hub application version. | 
**maxResults** | **Number** | Maximum number of input sources to be displayed per Resilience Hub application. | [optional] 
**nextToken** | **String** | Null, or the token from a previous call to get the next set of results. | [optional] 


