# TwilioProxy.ProxyV1Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. | [optional] 
**callbackUrl** | **String** | The URL we call when the interaction status changes. | [optional] 
**chatInstanceSid** | **String** | The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship. | [optional] 
**dateCreated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created. | [optional] 
**dateUpdated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. | [optional] 
**defaultTtl** | **Number** | The default &#x60;ttl&#x60; value for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value. | [optional] 
**geoMatchLevel** | [**ServiceEnumGeoMatchLevel**](ServiceEnumGeoMatchLevel.md) |  | [optional] 
**interceptCallbackUrl** | **String** | The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues. | [optional] 
**links** | **Object** | The URLs of resources related to the Service. | [optional] 
**numberSelectionBehavior** | [**ServiceEnumNumberSelectionBehavior**](ServiceEnumNumberSelectionBehavior.md) |  | [optional] 
**outOfSessionCallbackUrl** | **String** | The URL we call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information. | [optional] 
**sid** | **String** | The unique string that we created to identify the Service resource. | [optional] 
**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. Supports UTF-8 characters. **This value should not have PII.** | [optional] 
**url** | **String** | The absolute URL of the Service resource. | [optional] 


