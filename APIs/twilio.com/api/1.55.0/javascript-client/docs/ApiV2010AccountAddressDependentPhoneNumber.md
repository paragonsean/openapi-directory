# TwilioApi.ApiV2010AccountAddressDependentPhoneNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DependentPhoneNumber resource. | [optional] 
**addressRequirements** | [**DependentPhoneNumberEnumAddressRequirement**](DependentPhoneNumberEnumAddressRequirement.md) |  | [optional] 
**apiVersion** | **String** | The API version used to start a new TwiML session. | [optional] 
**capabilities** | **Object** | The set of Boolean properties that indicates whether a phone number can receive calls or messages.  Capabilities are  &#x60;Voice&#x60;, &#x60;SMS&#x60;, and &#x60;MMS&#x60; and each capability can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**emergencyAddressSid** | **String** | The SID of the emergency address configuration that we use for emergency calling from the phone number. | [optional] 
**emergencyStatus** | [**DependentPhoneNumberEnumEmergencyStatus**](DependentPhoneNumberEnumEmergencyStatus.md) |  | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**phoneNumber** | **String** | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**sid** | **String** | The unique string that that we created to identify the DependentPhoneNumber resource. | [optional] 
**smsApplicationSid** | **String** | The SID of the application that handles SMS messages sent to the phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all &#x60;sms_*_url&#x60; values and use those of the application. | [optional] 
**smsFallbackMethod** | **String** | The HTTP method we use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**smsFallbackUrl** | **String** | The URL that we call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] 
**smsMethod** | **String** | The HTTP method we use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**smsUrl** | **String** | The URL we call when the phone number receives an incoming SMS message. | [optional] 
**statusCallback** | **String** | The URL we call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
**statusCallbackMethod** | **String** | The HTTP method we use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**trunkSid** | **String** | The SID of the Trunk that handles calls to the phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 
**voiceApplicationSid** | **String** | The SID of the application that handles calls to the phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional] 
**voiceCallerIdLookup** | **Boolean** | Whether we look up the caller&#39;s caller-ID name from the CNAM database. Can be: &#x60;true&#x60; or &#x60;false&#x60;. Caller ID lookups can cost $0.01 each. | [optional] 
**voiceFallbackMethod** | **String** | The HTTP method we use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceFallbackUrl** | **String** | The URL that we call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] 
**voiceMethod** | **String** | The HTTP method we use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
**voiceUrl** | **String** | The URL we call when the phone number receives a call. The &#x60;voice_url&#x60; will not be used if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional] 



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




