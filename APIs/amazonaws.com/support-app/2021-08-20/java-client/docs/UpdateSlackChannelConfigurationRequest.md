

# UpdateSlackChannelConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelId** | **String** | The channel ID in Slack. This ID identifies a channel within a Slack workspace. |  |
|**channelName** | **String** | The Slack channel name that you want to update. |  [optional] |
|**channelRoleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations on Amazon Web Services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/support-app-permissions.html\&quot;&gt;Managing access to the Amazon Web Services Support App&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;. |  [optional] |
|**notifyOnAddCorrespondenceToCase** | **Boolean** | Whether you want to get notified when a support case has a new correspondence. |  [optional] |
|**notifyOnCaseSeverity** | [**NotifyOnCaseSeverityEnum**](#NotifyOnCaseSeverityEnum) | &lt;p&gt;The case severity for a support case that you want to receive notifications.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;high&lt;/code&gt; or &lt;code&gt;all&lt;/code&gt;, at least one of the following parameters must be &lt;code&gt;true&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;notifyOnAddCorrespondenceToCase&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;notifyOnCreateOrReopenCase&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;notifyOnResolveCase&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you specify &lt;code&gt;none&lt;/code&gt;, any of the following parameters that you specify in your request must be &lt;code&gt;false&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;notifyOnAddCorrespondenceToCase&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;notifyOnCreateOrReopenCase&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;notifyOnResolveCase&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;If you don&#39;t specify these parameters in your request, the Amazon Web Services Support App uses the current values by default.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**notifyOnCreateOrReopenCase** | **Boolean** | Whether you want to get notified when a support case is created or reopened. |  [optional] |
|**notifyOnResolveCase** | **Boolean** | Whether you want to get notified when a support case is resolved. |  [optional] |
|**teamId** | **String** | The team ID in Slack. This ID uniquely identifies a Slack workspace, such as &lt;code&gt;T012ABCDEFG&lt;/code&gt;. |  |



## Enum: NotifyOnCaseSeverityEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| ALL | &quot;all&quot; |
| HIGH | &quot;high&quot; |



