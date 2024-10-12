# TwilioApi.ApiV2010AccountSipSipDomain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource. | [optional] 
**apiVersion** | **String** | The API version used to process the call. | [optional] 
**authType** | **String** | The types of authentication you have mapped to your domain. Can be: &#x60;IP_ACL&#x60; and &#x60;CREDENTIAL_LIST&#x60;. If you have both defined for your domain, both will be returned in a comma delimited string. If &#x60;auth_type&#x60; is not defined, the domain will not be able to receive any traffic. | [optional] 
**byocTrunkSid** | **String** | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**domainName** | **String** | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \&quot;-\&quot; and must end with &#x60;sip.twilio.com&#x60;. | [optional] 
**emergencyCallerSid** | **String** | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional] 
**emergencyCallingEnabled** | **Boolean** | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**secure** | **Boolean** | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional] 
**sid** | **String** | The unique string that that we created to identify the SipDomain resource. | [optional] 
**sipRegistration** | **Boolean** | Whether to allow SIP Endpoints to register with the domain to receive calls. | [optional] 
**subresourceUris** | **Object** | A list of mapping resources associated with the SIP Domain resource identified by their relative URIs. | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 
**voiceFallbackMethod** | **String** | The HTTP method we use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceFallbackUrl** | **String** | The URL that we call when an error occurs while retrieving or executing the TwiML requested from &#x60;voice_url&#x60;. | [optional] 
**voiceMethod** | **String** | The HTTP method we use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceStatusCallbackMethod** | **String** | The HTTP method we use to call &#x60;voice_status_callback_url&#x60;. Either &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceStatusCallbackUrl** | **String** | The URL that we call to pass status parameters (such as call ended) to your application. | [optional] 
**voiceUrl** | **String** | The URL we call using the &#x60;voice_method&#x60; when the domain receives a call. | [optional] 



## Enum: VoiceFallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)





## Enum: VoiceMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)





## Enum: VoiceStatusCallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)




