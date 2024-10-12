

# TrunkingV1TrunkPhoneNumber


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PhoneNumber resource. |  [optional] |
|**addressRequirements** | **PhoneNumberEnumAddressRequirement** |  |  [optional] |
|**apiVersion** | **String** | The API version used to start a new TwiML session. |  [optional] |
|**beta** | **Boolean** | Whether the phone number is new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60;. |  [optional] |
|**capabilities** | **Object** | The set of Boolean properties that indicate whether a phone number can receive calls or messages.  Capabilities are  &#x60;Voice&#x60;, &#x60;SMS&#x60;, and &#x60;MMS&#x60; and each capability can be: &#x60;true&#x60; or &#x60;false&#x60;. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**phoneNumber** | **String** | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the PhoneNumber resource. |  [optional] |
|**smsApplicationSid** | **String** | The SID of the application that handles SMS messages sent to the phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all &#x60;sms_*_url&#x60; values and use those of the application. |  [optional] |
|**smsFallbackMethod** | [**SmsFallbackMethodEnum**](#SmsFallbackMethodEnum) | The HTTP method we use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**smsFallbackUrl** | **URI** | The URL that we call using the &#x60;sms_fallback_method&#x60; when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. |  [optional] |
|**smsMethod** | [**SmsMethodEnum**](#SmsMethodEnum) | The HTTP method we use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**smsUrl** | **URI** | The URL we call using the &#x60;sms_method&#x60; when the phone number receives an incoming SMS message. |  [optional] |
|**statusCallback** | **URI** | The URL we call using the &#x60;status_callback_method&#x60; to send status information to your application. |  [optional] |
|**statusCallbackMethod** | [**StatusCallbackMethodEnum**](#StatusCallbackMethodEnum) | The HTTP method we use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**trunkSid** | **String** | The SID of the Trunk that handles calls to the phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice URLs and voice applications and use those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**voiceApplicationSid** | **String** | The SID of the application that handles calls to the phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice URLs and use those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. |  [optional] |
|**voiceCallerIdLookup** | **Boolean** | Whether we look up the caller&#39;s caller-ID name from the CNAM database ($0.01 per look up). Can be: &#x60;true&#x60; or &#x60;false&#x60;. |  [optional] |
|**voiceFallbackMethod** | [**VoiceFallbackMethodEnum**](#VoiceFallbackMethodEnum) | The HTTP method that we use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**voiceFallbackUrl** | **URI** | The URL that we call using the &#x60;voice_fallback_method&#x60; when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. |  [optional] |
|**voiceMethod** | [**VoiceMethodEnum**](#VoiceMethodEnum) | The HTTP method we use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. |  [optional] |
|**voiceUrl** | **URI** | The URL we call using the &#x60;voice_method&#x60; when the phone number receives a call. The &#x60;voice_url&#x60; is not be used if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. |  [optional] |



## Enum: SmsFallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: SmsMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: StatusCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: VoiceFallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: VoiceMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



