# AmazonCloudWatchLogs.PutRetentionPolicyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logGroupName** | **String** |  | 
**retentionInDays** | **Number** | &lt;p&gt;The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.&lt;/p&gt; &lt;p&gt;To set a log group so that its log events do not expire, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html\&quot;&gt;DeleteRetentionPolicy&lt;/a&gt;. &lt;/p&gt; | 


