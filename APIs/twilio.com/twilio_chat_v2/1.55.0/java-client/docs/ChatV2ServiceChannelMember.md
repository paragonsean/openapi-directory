

# ChatV2ServiceChannelMember


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource. |  [optional] |
|**attributes** | **String** | The JSON string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. |  [optional] |
|**channelSid** | **String** | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource belongs to. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info. |  [optional] |
|**lastConsumedMessageIndex** | **Integer** | The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read. |  [optional] |
|**lastConsumptionTimestamp** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels). |  [optional] |
|**roleSid** | **String** | The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) assigned to the member. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Member resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Member resource. |  [optional] |
|**url** | **URI** | The absolute URL of the Member resource. |  [optional] |



