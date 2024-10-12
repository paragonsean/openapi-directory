

# WirelessV1Sim


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the Sim resource belongs. |  [optional] |
|**commandsCallbackMethod** | [**CommandsCallbackMethodEnum**](#CommandsCallbackMethodEnum) | The HTTP method we use to call &#x60;commands_callback_url&#x60;.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60;. Default is &#x60;POST&#x60;. |  [optional] |
|**commandsCallbackUrl** | **URI** | The URL we call using the &#x60;commands_callback_method&#x60; when the SIM originates a machine-to-machine [Command](https://www.twilio.com/docs/iot/wireless/api/command-resource). Your server should respond with an HTTP status code in the 200 range; any response body will be ignored. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the Sim resource was last updated specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |  [optional] |
|**eId** | **String** | Deprecated. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the Sim resource. |  [optional] |
|**iccid** | **String** | The [ICCID](https://en.wikipedia.org/wiki/SIM_card#ICCID) associated with the SIM. |  [optional] |
|**ipAddress** | **String** | Deprecated. |  [optional] |
|**links** | **Object** | The URLs of related subresources. |  [optional] |
|**ratePlanSid** | **String** | The SID of the [RatePlan resource](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource) to which the Sim resource is assigned. |  [optional] |
|**resetStatus** | **SimEnumResetStatus** |  |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Sim resource. |  [optional] |
|**smsFallbackMethod** | [**SmsFallbackMethodEnum**](#SmsFallbackMethodEnum) | Deprecated. |  [optional] |
|**smsFallbackUrl** | **URI** | Deprecated. |  [optional] |
|**smsMethod** | [**SmsMethodEnum**](#SmsMethodEnum) | Deprecated. |  [optional] |
|**smsUrl** | **URI** | Deprecated. |  [optional] |
|**status** | **SimEnumStatus** |  |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**voiceFallbackMethod** | [**VoiceFallbackMethodEnum**](#VoiceFallbackMethodEnum) | Deprecated. The HTTP method we use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. |  [optional] |
|**voiceFallbackUrl** | **URI** | Deprecated. The URL we call using the &#x60;voice_fallback_method&#x60; when an error occurs while retrieving or executing the TwiML requested from &#x60;voice_url&#x60;. |  [optional] |
|**voiceMethod** | [**VoiceMethodEnum**](#VoiceMethodEnum) | Deprecated. The HTTP method we use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. |  [optional] |
|**voiceUrl** | **URI** | Deprecated. The URL we call using the &#x60;voice_method&#x60; when the SIM-connected device makes a voice call. |  [optional] |



## Enum: CommandsCallbackMethodEnum

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PATCH | &quot;PATCH&quot; |
| PUT | &quot;PUT&quot; |
| DELETE | &quot;DELETE&quot; |



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



