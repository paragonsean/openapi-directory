

# CreateRealtimeLogConfig20200531Request


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endPoints** | [**List&lt;EndPoint&gt;**](EndPoint.md) | Contains information about the Amazon Kinesis data stream where you are sending real-time log data. |  |
|**fields** | [**List&lt;String&gt;**](String.md) | &lt;p&gt;A list of fields to include in each real-time log record.&lt;/p&gt; &lt;p&gt;For more information about fields, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html#understand-real-time-log-config-fields\&quot;&gt;Real-time log configuration fields&lt;/a&gt; in the &lt;i&gt;Amazon CloudFront Developer Guide&lt;/i&gt;.&lt;/p&gt; |  |
|**name** | **String** | A unique name to identify this real-time log configuration. |  |
|**samplingRate** | **Integer** | The sampling rate for this real-time log configuration. The sampling rate determines the percentage of viewer requests that are represented in the real-time log data. You must provide an integer between 1 and 100, inclusive. |  |



