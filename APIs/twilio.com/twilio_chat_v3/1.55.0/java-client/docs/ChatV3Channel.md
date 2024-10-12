

# ChatV3Channel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Channel resource. |  [optional] |
|**attributes** | **String** | The JSON string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. |  [optional] |
|**createdBy** | **String** | The &#x60;identity&#x60; of the User that created the channel. If the Channel was created by using the API, the value is &#x60;system&#x60;. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**membersCount** | **Integer** | The number of Members in the Channel. |  [optional] |
|**messagesCount** | **Integer** | The number of Messages that have been passed in the Channel. |  [optional] |
|**messagingServiceSid** | **String** | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Channel resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Channel resource. |  [optional] |
|**type** | **ChannelEnumChannelType** |  |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. |  [optional] |
|**url** | **URI** | The absolute URL of the Channel resource. |  [optional] |



