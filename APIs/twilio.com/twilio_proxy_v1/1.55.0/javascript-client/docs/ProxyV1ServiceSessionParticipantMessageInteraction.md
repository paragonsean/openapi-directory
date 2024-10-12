# TwilioProxy.ProxyV1ServiceSessionParticipantMessageInteraction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the MessageInteraction resource. | [optional] 
**data** | **String** | A JSON string that includes the message body sent to the participant. (e.g. &#x60;{\&quot;body\&quot;: \&quot;hello\&quot;}&#x60;) | [optional] 
**dateCreated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created. | [optional] 
**dateUpdated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. | [optional] 
**inboundParticipantSid** | **String** | Always empty for created Message Interactions. | [optional] 
**inboundResourceSid** | **String** | Always empty for created Message Interactions. | [optional] 
**inboundResourceStatus** | [**MessageInteractionEnumResourceStatus**](MessageInteractionEnumResourceStatus.md) |  | [optional] 
**inboundResourceType** | **String** | Always empty for created Message Interactions. | [optional] 
**inboundResourceUrl** | **String** | Always empty for created Message Interactions. | [optional] 
**outboundParticipantSid** | **String** | The SID of the outbound [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | [optional] 
**outboundResourceSid** | **String** | The SID of the outbound [Message](https://www.twilio.com/docs/sms/api/message-resource) resource. | [optional] 
**outboundResourceStatus** | [**MessageInteractionEnumResourceStatus**](MessageInteractionEnumResourceStatus.md) |  | [optional] 
**outboundResourceType** | **String** | The outbound resource type. This value is always &#x60;Message&#x60;. | [optional] 
**outboundResourceUrl** | **String** | The URL of the Twilio message resource. | [optional] 
**participantSid** | **String** | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | [optional] 
**serviceSid** | **String** | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | [optional] 
**sessionSid** | **String** | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource. | [optional] 
**sid** | **String** | The unique string that we created to identify the MessageInteraction resource. | [optional] 
**type** | [**MessageInteractionEnumType**](MessageInteractionEnumType.md) |  | [optional] 
**url** | **String** | The absolute URL of the MessageInteraction resource. | [optional] 


