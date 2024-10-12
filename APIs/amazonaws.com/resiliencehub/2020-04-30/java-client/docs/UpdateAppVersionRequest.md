

# UpdateAppVersionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfo** | **Map&lt;String, List&lt;String&gt;&gt;** | &lt;p&gt;Additional configuration parameters for an Resilience Hub application. If you want to implement &lt;code&gt;additionalInfo&lt;/code&gt; through the Resilience Hub console rather than using an API call, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html\&quot;&gt;Configure the application configuration parameters&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.&lt;/p&gt; &lt;p&gt;Key: &lt;code&gt;\&quot;failover-regions\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Value: &lt;code&gt;\&quot;[{\&quot;region\&quot;:\&quot;&amp;lt;REGION&amp;gt;\&quot;, \&quot;accounts\&quot;:[{\&quot;id\&quot;:\&quot;&amp;lt;ACCOUNT_ID&amp;gt;\&quot;}]}]\&quot;&lt;/code&gt; &lt;/p&gt; &lt;/note&gt; |  [optional] |
|**appArn** | **String** | Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:&lt;code&gt;partition&lt;/code&gt;:resiliencehub:&lt;code&gt;region&lt;/code&gt;:&lt;code&gt;account&lt;/code&gt;:app/&lt;code&gt;app-id&lt;/code&gt;. For more information about ARNs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt; Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;AWS General Reference&lt;/i&gt; guide. |  |



