# FirebaseCloudMessagingApi.Message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android** | [**AndroidConfig**](AndroidConfig.md) |  | [optional] 
**apns** | [**ApnsConfig**](ApnsConfig.md) |  | [optional] 
**condition** | **String** | Condition to send a message to, e.g. \&quot;&#39;foo&#39; in topics &amp;&amp; &#39;bar&#39; in topics\&quot;. | [optional] 
**data** | **{String: String}** | Input only. Arbitrary key/value payload, which must be UTF-8 encoded. The key should not be a reserved word (\&quot;from\&quot;, \&quot;message_type\&quot;, or any word starting with \&quot;google\&quot; or \&quot;gcm\&quot;). When sending payloads containing only data fields to iOS devices, only normal priority (&#x60;\&quot;apns-priority\&quot;: \&quot;5\&quot;&#x60;) is allowed in [&#x60;ApnsConfig&#x60;](/docs/reference/fcm/rest/v1/projects.messages#apnsconfig). | [optional] 
**fcmOptions** | [**FcmOptions**](FcmOptions.md) |  | [optional] 
**name** | **String** | Output Only. The identifier of the message sent, in the format of &#x60;projects/_*_/messages/{message_id}&#x60;. | [optional] 
**notification** | [**Notification**](Notification.md) |  | [optional] 
**token** | **String** | Registration token to send a message to. | [optional] 
**topic** | **String** | Topic name to send a message to, e.g. \&quot;weather\&quot;. Note: \&quot;/topics/\&quot; prefix should not be provided. | [optional] 
**webpush** | [**WebpushConfig**](WebpushConfig.md) |  | [optional] 


