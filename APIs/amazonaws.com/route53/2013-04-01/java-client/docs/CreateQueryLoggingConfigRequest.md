

# CreateQueryLoggingConfigRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostedZoneId** | **String** | The ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones. |  |
|**cloudWatchLogsLogGroupArn** | **String** | &lt;p&gt;The Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:&lt;/p&gt; &lt;p&gt;arn:aws:logs:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:log-group:&lt;i&gt;log_group_name&lt;/i&gt; &lt;/p&gt; &lt;p&gt;To get the ARN for a log group, you can use the CloudWatch console, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html\&quot;&gt;DescribeLogGroups&lt;/a&gt; API action, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/logs/describe-log-groups.html\&quot;&gt;describe-log-groups&lt;/a&gt; command, or the applicable command in one of the Amazon Web Services SDKs.&lt;/p&gt; |  |



