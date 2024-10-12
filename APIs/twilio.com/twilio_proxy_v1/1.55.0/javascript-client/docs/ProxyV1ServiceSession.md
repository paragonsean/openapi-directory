# TwilioProxy.ProxyV1ServiceSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Session resource. | [optional] 
**closedReason** | **String** | The reason the Session ended. | [optional] 
**dateCreated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created. | [optional] 
**dateEnded** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session ended. | [optional] 
**dateExpiry** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value. | [optional] 
**dateLastInteraction** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session last had an interaction. | [optional] 
**dateStarted** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session started. | [optional] 
**dateUpdated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. | [optional] 
**links** | **Object** | The URLs of resources related to the Session. | [optional] 
**mode** | [**SessionEnumMode**](SessionEnumMode.md) |  | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/proxy/api/service) the session is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Session resource. | [optional] 
**status** | [**SessionEnumStatus**](SessionEnumStatus.md) |  | [optional] 
**ttl** | **Number** | The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction. | [optional] 
**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. Supports UTF-8 characters. **This value should not have PII.** | [optional] 
**url** | **String** | The absolute URL of the Session resource. | [optional] 


