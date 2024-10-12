# TwilioChat.ChatV2ServiceChannel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Channel resource. | [optional] 
**attributes** | **String** | The JSON string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] 
**createdBy** | **String** | The &#x60;identity&#x60; of the User that created the channel. If the Channel was created by using the API, the value is &#x60;system&#x60;. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**links** | **Object** | The absolute URLs of the [Members](https://www.twilio.com/docs/chat/rest/member-resource), [Messages](https://www.twilio.com/docs/chat/rest/message-resource), [Invites](https://www.twilio.com/docs/chat/rest/invite-resource), Webhooks and, if it exists, the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) for the Channel. | [optional] 
**membersCount** | **Number** | The number of Members in the Channel. | [optional] 
**messagesCount** | **Number** | The number of Messages that have been passed in the Channel. | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Channel resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Channel resource. | [optional] 
**type** | [**ChannelEnumChannelType**](ChannelEnumChannelType.md) |  | [optional] 
**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] 
**url** | **String** | The absolute URL of the Channel resource. | [optional] 


