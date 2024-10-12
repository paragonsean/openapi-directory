

# ChatV1ServiceChannelMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Message resource. |  [optional] |
|**attributes** | **String** | The JSON string that stores application-specific data. **Note** If this property has been assigned a value, it&#39;s only  displayed in a FETCH action that returns a single resource; otherwise, it&#39;s null. If the attributes have not been set, &#x60;{}&#x60; is returned. |  [optional] |
|**body** | **String** | The content of the message. |  [optional] |
|**channelSid** | **String** | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the Message resource belongs to. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**from** | **String** | The [identity](https://www.twilio.com/docs/api/chat/guides/identity) of the message&#39;s author. The default value is &#x60;system&#x60;. |  [optional] |
|**index** | **Integer** | The index of the message within the [Channel](https://www.twilio.com/docs/chat/api/channels). |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Message resource. |  [optional] |
|**to** | **String** | The SID of the [Channel](https://www.twilio.com/docs/chat/api/channels) that the message was sent to. |  [optional] |
|**url** | **URI** | The absolute URL of the Message resource. |  [optional] |
|**wasEdited** | **Boolean** | Whether the message has been edited since it was created. |  [optional] |



