

# ChatV1ServiceChannel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Channel resource. |  [optional] |
|**attributes** | **String** | The JSON string that stores application-specific data. **Note** If this property has been assigned a value, it&#39;s only  displayed in a FETCH action that returns a single resource; otherwise, it&#39;s null. If the attributes have not been set, &#x60;{}&#x60; is returned. |  [optional] |
|**createdBy** | **String** | The &#x60;identity&#x60; of the User that created the channel. If the Channel was created by using the API, the value is &#x60;system&#x60;. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**links** | **Object** | The absolute URLs of the [Members](https://www.twilio.com/docs/chat/api/members), [Messages](https://www.twilio.com/docs/chat/api/messages) , [Invites](https://www.twilio.com/docs/chat/api/invites) and, if it exists, the last [Message](https://www.twilio.com/docs/chat/api/messages) for the Channel. |  [optional] |
|**membersCount** | **Integer** | The number of Members in the Channel. |  [optional] |
|**messagesCount** | **Integer** | The number of Messages in the Channel. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Channel resource. |  [optional] |
|**type** | **ChannelEnumChannelType** |  |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. |  [optional] |
|**url** | **URI** | The absolute URL of the Channel resource. |  [optional] |



