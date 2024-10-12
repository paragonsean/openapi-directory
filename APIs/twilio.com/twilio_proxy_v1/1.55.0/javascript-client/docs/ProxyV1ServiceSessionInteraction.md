# TwilioProxy.ProxyV1ServiceSessionInteraction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Interaction resource. | [optional] 
**data** | **String** | A JSON string that includes the message body of message interactions (e.g. &#x60;{\&quot;body\&quot;: \&quot;hello\&quot;}&#x60;) or the call duration (when available) of a call (e.g. &#x60;{\&quot;duration\&quot;: \&quot;5\&quot;}&#x60;). | [optional] 
**dateCreated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Interaction was created. | [optional] 
**dateUpdated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. | [optional] 
**inboundParticipantSid** | **String** | The SID of the inbound [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | [optional] 
**inboundResourceSid** | **String** | The SID of the inbound resource; either the [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource). | [optional] 
**inboundResourceStatus** | [**InteractionEnumResourceStatus**](InteractionEnumResourceStatus.md) |  | [optional] 
**inboundResourceType** | **String** | The inbound resource type. Can be [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource). | [optional] 
**inboundResourceUrl** | **String** | The URL of the Twilio inbound resource | [optional] 
**outboundParticipantSid** | **String** | The SID of the outbound [Participant](https://www.twilio.com/docs/proxy/api/participant)). | [optional] 
**outboundResourceSid** | **String** | The SID of the outbound resource; either the [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource). | [optional] 
**outboundResourceStatus** | [**InteractionEnumResourceStatus**](InteractionEnumResourceStatus.md) |  | [optional] 
**outboundResourceType** | **String** | The outbound resource type. Can be: [Call](https://www.twilio.com/docs/voice/api/call-resource) or [Message](https://www.twilio.com/docs/sms/api/message-resource). | [optional] 
**outboundResourceUrl** | **String** | The URL of the Twilio outbound resource. | [optional] 
**serviceSid** | **String** | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | [optional] 
**sessionSid** | **String** | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource. | [optional] 
**sid** | **String** | The unique string that we created to identify the Interaction resource. | [optional] 
**type** | [**InteractionEnumType**](InteractionEnumType.md) |  | [optional] 
**url** | **String** | The absolute URL of the Interaction resource. | [optional] 


