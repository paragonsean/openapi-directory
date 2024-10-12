

# CreateMeetingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRequestToken** | **String** | The unique identifier for the client request. Use a different token for different meetings. |  |
|**externalMeetingId** | **String** | The external meeting ID. |  [optional] |
|**meetingHostId** | **String** | Reserved. |  [optional] |
|**mediaRegion** | **String** | &lt;p&gt; The Region in which to create the meeting. Default: &lt;code&gt;us-east-1&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; Available values: &lt;code&gt;af-south-1&lt;/code&gt; , &lt;code&gt;ap-northeast-1&lt;/code&gt; , &lt;code&gt;ap-northeast-2&lt;/code&gt; , &lt;code&gt;ap-south-1&lt;/code&gt; , &lt;code&gt;ap-southeast-1&lt;/code&gt; , &lt;code&gt;ap-southeast-2&lt;/code&gt; , &lt;code&gt;ca-central-1&lt;/code&gt; , &lt;code&gt;eu-central-1&lt;/code&gt; , &lt;code&gt;eu-north-1&lt;/code&gt; , &lt;code&gt;eu-south-1&lt;/code&gt; , &lt;code&gt;eu-west-1&lt;/code&gt; , &lt;code&gt;eu-west-2&lt;/code&gt; , &lt;code&gt;eu-west-3&lt;/code&gt; , &lt;code&gt;sa-east-1&lt;/code&gt; , &lt;code&gt;us-east-1&lt;/code&gt; , &lt;code&gt;us-east-2&lt;/code&gt; , &lt;code&gt;us-west-1&lt;/code&gt; , &lt;code&gt;us-west-2&lt;/code&gt; . &lt;/p&gt; |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tag key-value pairs. |  [optional] |
|**notificationsConfiguration** | [**CreateMeetingRequestNotificationsConfiguration**](CreateMeetingRequestNotificationsConfiguration.md) |  |  [optional] |



