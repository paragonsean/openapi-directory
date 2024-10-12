# TwilioApi.ApiV2010AccountApplication

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource. | [optional] 
**apiVersion** | **String** | The API version used to start a new TwiML session. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**messageStatusCallback** | **String** | The URL we call using a POST method to send message status information to your application. | [optional] 
**publicApplicationConnectEnabled** | **Boolean** | Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
**sid** | **String** | The unique string that that we created to identify the Application resource. | [optional] 
**smsFallbackMethod** | **String** | The HTTP method we use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**smsFallbackUrl** | **String** | The URL that we call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] 
**smsMethod** | **String** | The HTTP method we use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**smsStatusCallback** | **String** | The URL we call using a POST method to send status information to your application about SMS messages that refer to the application. | [optional] 
**smsUrl** | **String** | The URL we call when the phone number receives an incoming SMS message. | [optional] 
**statusCallback** | **String** | The URL we call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
**statusCallbackMethod** | **String** | The HTTP method we use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 
**voiceCallerIdLookup** | **Boolean** | Whether we look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
**voiceFallbackMethod** | **String** | The HTTP method we use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceFallbackUrl** | **String** | The URL that we call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] 
**voiceMethod** | **String** | The HTTP method we use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceUrl** | **String** | The URL we call when the phone number assigned to this application receives a call. | [optional] 



## Enum: SmsFallbackMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)





## Enum: SmsMethodEnum


* `HEAD` (value: `"HEAD"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PATCH` (value: `"PATCH"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)





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




