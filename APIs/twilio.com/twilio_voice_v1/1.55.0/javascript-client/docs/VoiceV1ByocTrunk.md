# TwilioVoice.VoiceV1ByocTrunk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the BYOC Trunk resource. | [optional] 
**cnamLookupEnabled** | **Boolean** | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] 
**connectionPolicySid** | **String** | The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure. | [optional] 
**dateCreated** | **Date** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**fromDomainSid** | **String** | The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \&quot;call back\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \&quot;sip.twilio.com\&quot;. | [optional] 
**sid** | **String** | The unique string that that we created to identify the BYOC Trunk resource. | [optional] 
**statusCallbackMethod** | **String** | The HTTP method we use to call &#x60;status_callback_url&#x60;. Either &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**statusCallbackUrl** | **String** | The URL that we call to pass status parameters (such as call ended) to your application. | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 
**voiceFallbackMethod** | **String** | The HTTP method we use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceFallbackUrl** | **String** | The URL that we call when an error occurs while retrieving or executing the TwiML requested from &#x60;voice_url&#x60;. | [optional] 
**voiceMethod** | **String** | The HTTP method we use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceUrl** | **String** | The URL we call using the &#x60;voice_method&#x60; when the BYOC Trunk receives a call. | [optional] 



## Enum: StatusCallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)





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




