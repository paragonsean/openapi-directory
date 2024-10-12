

# CreateFeatureRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultVariation** | **String** | &lt;p&gt;The name of the variation to use as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature.&lt;/p&gt; &lt;p&gt;This variation must also be listed in the &lt;code&gt;variations&lt;/code&gt; structure.&lt;/p&gt; &lt;p&gt;If you omit &lt;code&gt;defaultVariation&lt;/code&gt;, the first variation listed in the &lt;code&gt;variations&lt;/code&gt; structure is used as the default variation.&lt;/p&gt; |  [optional] |
|**description** | **String** | An optional description of the feature. |  [optional] |
|**entityOverrides** | **Map&lt;String, String&gt;** | &lt;p&gt;Specify users that should always be served a specific variation of a feature. Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.&lt;/p&gt; &lt;p&gt;This parameter is limited to 2500 overrides or a total of 40KB. The 40KB limit includes an overhead of 6 bytes per override.&lt;/p&gt; |  [optional] |
|**evaluationStrategy** | [**EvaluationStrategyEnum**](#EvaluationStrategyEnum) | Specify &lt;code&gt;ALL_RULES&lt;/code&gt; to activate the traffic allocation specified by any ongoing launches or experiments. Specify &lt;code&gt;DEFAULT_VARIATION&lt;/code&gt; to serve the default variation to all users instead. |  [optional] |
|**name** | **String** | The name for the new feature. |  |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;Assigns one or more tags (key-value pairs) to the feature.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a feature.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**variations** | [**List&lt;VariationConfig&gt;**](VariationConfig.md) | An array of structures that contain the configuration of the feature&#39;s different variations. |  |



## Enum: EvaluationStrategyEnum

| Name | Value |
|---- | -----|
| ALL_RULES | &quot;ALL_RULES&quot; |
| DEFAULT_VARIATION | &quot;DEFAULT_VARIATION&quot; |



