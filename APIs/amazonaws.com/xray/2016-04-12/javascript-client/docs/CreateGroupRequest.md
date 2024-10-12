# AwsXRay.CreateGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupName** | **String** | The case-sensitive name of the new group. Default is a reserved name and names must be unique. | 
**filterExpression** | **String** | The filter expression defining criteria by which to group traces. | [optional] 
**insightsConfiguration** | [**CreateGroupRequestInsightsConfiguration**](CreateGroupRequestInsightsConfiguration.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | &lt;p&gt;A map that contains one or more tag keys and tag values to attach to an X-Ray group. For more information about ways to use tags, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The following restrictions apply to tags:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum number of user-applied tags per resource: 50&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum tag key length: 128 Unicode characters&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum tag value length: 256 Unicode characters&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / &#x3D; + - and @&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Tag keys and values are case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Don&#39;t use &lt;code&gt;aws:&lt;/code&gt; as a prefix for keys; it&#39;s reserved for Amazon Web Services use.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 


