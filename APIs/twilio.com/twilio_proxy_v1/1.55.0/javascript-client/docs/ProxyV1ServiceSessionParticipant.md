# TwilioProxy.ProxyV1ServiceSessionParticipant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource. | [optional] 
**dateCreated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created. | [optional] 
**dateDeleted** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Participant was removed from the session. | [optional] 
**dateUpdated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the participant. This value must be 255 characters or fewer. Supports UTF-8 characters. **This value should not have PII.** | [optional] 
**identifier** | **String** | The phone number or channel identifier of the Participant. This value must be 191 characters or fewer. Supports UTF-8 characters. | [optional] 
**links** | **Object** | The URLs to resources related the participant. | [optional] 
**proxyIdentifier** | **String** | The phone number or short code (masked number) of the participant&#39;s partner. The participant will call or message the partner participant at this number. | [optional] 
**proxyIdentifierSid** | **String** | The SID of the Proxy Identifier assigned to the Participant. | [optional] 
**serviceSid** | **String** | The SID of the resource&#39;s parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | [optional] 
**sessionSid** | **String** | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource. | [optional] 
**sid** | **String** | The unique string that we created to identify the Participant resource. | [optional] 
**url** | **String** | The absolute URL of the Participant resource. | [optional] 


