

# ConfigureLogsForPlaybackConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**percentEnabled** | **Integer** | &lt;p&gt;The percentage of session logs that MediaTailor sends to your Cloudwatch Logs account. For example, if your playback configuration has 1000 sessions and percentEnabled is set to &lt;code&gt;60&lt;/code&gt;, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html\&quot;&gt;debug log mode&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;0&lt;/code&gt; - &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; |  |
|**playbackConfigurationName** | **String** | The name of the playback configuration. |  |



