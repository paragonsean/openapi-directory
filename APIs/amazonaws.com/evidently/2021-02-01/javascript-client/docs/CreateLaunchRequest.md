# AmazonCloudWatchEvidently.CreateLaunchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | An optional description for the launch. | [optional] 
**groups** | [**[LaunchGroupConfig]**](LaunchGroupConfig.md) | An array of structures that contains the feature and variations that are to be used for the launch. | 
**metricMonitors** | [**[MetricMonitorConfig]**](MetricMonitorConfig.md) | An array of structures that define the metrics that will be used to monitor the launch performance. | [optional] 
**name** | **String** | The name for the new launch. | 
**randomizationSalt** | **String** | When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and &lt;code&gt;randomizationSalt&lt;/code&gt;. If you omit &lt;code&gt;randomizationSalt&lt;/code&gt;, Evidently uses the launch name as the &lt;code&gt;randomizationSalt&lt;/code&gt;. | [optional] 
**scheduledSplitsConfig** | [**CreateLaunchRequestScheduledSplitsConfig**](CreateLaunchRequestScheduledSplitsConfig.md) |  | [optional] 
**tags** | **{String: String}** | &lt;p&gt;Assigns one or more tags (key-value pairs) to the launch.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a launch.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt; | [optional] 


