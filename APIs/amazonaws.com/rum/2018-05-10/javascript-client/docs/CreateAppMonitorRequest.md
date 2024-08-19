# CloudWatchRum.CreateAppMonitorRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appMonitorConfiguration** | [**CreateAppMonitorRequestAppMonitorConfiguration**](CreateAppMonitorRequestAppMonitorConfiguration.md) |  | [optional] 
**customEvents** | [**CreateAppMonitorRequestCustomEvents**](CreateAppMonitorRequestCustomEvents.md) |  | [optional] 
**cwLogEnabled** | **Boolean** | &lt;p&gt;Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.&lt;/p&gt; &lt;p&gt;If you omit this parameter, the default is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt; | [optional] 
**domain** | **String** | The top-level internet domain name for which your application has administrative authority. | 
**name** | **String** | A name for the app monitor. | 
**tags** | **{String: String}** | &lt;p&gt;Assigns one or more tags (key-value pairs) to the app monitor.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with an app monitor.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services resources&lt;/a&gt;.&lt;/p&gt; | [optional] 


