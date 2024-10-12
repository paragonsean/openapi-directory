# TwilioChat.ChatV1ServiceChannelMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Member resource. | [optional] 
**channelSid** | **String** | The unique ID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) for the member. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s [User](https://www.twilio.com/docs/api/chat/rest/users) within the [Service](https://www.twilio.com/docs/api/chat/rest/services). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info. | [optional] 
**lastConsumedMessageIndex** | **Number** | The index of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) in the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) that the Member has read. | [optional] 
**lastConsumptionTimestamp** | **Date** | The ISO 8601 timestamp string that represents the date-time of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) read event for the Member within the [Channel](https://www.twilio.com/docs/api/chat/rest/channels). | [optional] 
**roleSid** | **String** | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the member. | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Member resource. | [optional] 
**url** | **String** | The absolute URL of the Member resource. | [optional] 


