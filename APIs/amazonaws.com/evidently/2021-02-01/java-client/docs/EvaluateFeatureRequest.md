

# EvaluateFeatureRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityId** | **String** | An internal ID that represents a unique user of the application. This &lt;code&gt;entityID&lt;/code&gt; is checked against any override rules assigned for this feature. |  |
|**evaluationContext** | **String** | &lt;p&gt;A JSON object of attributes that you can optionally pass in as part of the evaluation event sent to Evidently from the user session. Evidently can use this value to match user sessions with defined audience segments. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html\&quot;&gt;Use segments to focus your audience&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you include this parameter, the value must be a JSON object. A JSON array is not supported.&lt;/p&gt; |  [optional] |



