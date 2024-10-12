# CloudWatchObservabilityAccessManager.CreateLinkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labelTemplate** | **String** | &lt;p&gt;Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.&lt;/p&gt; &lt;p&gt;You can use a custom label or use the following variables:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;$AccountName&lt;/code&gt; is the name of the account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;$AccountEmail&lt;/code&gt; is the globally unique email address of the account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;$AccountEmailNoDomain&lt;/code&gt; is the email address of the account without the domain name&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**resourceTypes** | [**[ResourceType]**](ResourceType.md) | An array of strings that define which types of data that the source account shares with the monitoring account. | 
**sinkIdentifier** | **String** | &lt;p&gt;The ARN of the sink to use to create this link. You can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html\&quot;&gt;ListSinks&lt;/a&gt; to find the ARNs of sinks.&lt;/p&gt; &lt;p&gt;For more information about sinks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html\&quot;&gt;CreateSink&lt;/a&gt;.&lt;/p&gt; | 
**tags** | **{String: String}** | &lt;p&gt;Assigns one or more tags (key-value pairs) to the link. &lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;For more information about using tags to control access, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\&quot;&gt;Controlling access to Amazon Web Services resources using tags&lt;/a&gt;.&lt;/p&gt; | [optional] 


