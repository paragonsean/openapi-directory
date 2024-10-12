

# VerifyV2Service


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. |  [optional] |
|**codeLength** | **Integer** | The length of the verification code to generate. |  [optional] |
|**customCodeEnabled** | **Boolean** | Whether to allow sending verifications with a custom code instead of a randomly generated one. Not available for all customers. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**defaultTemplateSid** | **String** |  |  [optional] |
|**doNotShareWarningEnabled** | **Boolean** | Whether to add a security warning at the end of an SMS verification body. Disabled by default and applies only to SMS. Example SMS body: &#x60;Your AppName verification code is: 1234. Don’t share this code with anyone; our employees will never ask for the code&#x60; |  [optional] |
|**dtmfInputRequired** | **Boolean** | Whether to ask the user to press a number before delivering the verify code in a phone call. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the verification service. It can be up to 32 characters long. **This value should not contain PII.** |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**lookupEnabled** | **Boolean** | Whether to perform a lookup with each verification started and return info about the phone number. |  [optional] |
|**psd2Enabled** | **Boolean** | Whether to pass PSD2 transaction parameters when starting a verification. |  [optional] |
|**push** | **Object** | Configurations for the Push factors (channel) created under this Service. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Service resource. |  [optional] |
|**skipSmsToLandlines** | **Boolean** | Whether to skip sending SMS verifications to landlines. Requires &#x60;lookup_enabled&#x60;. |  [optional] |
|**totp** | **Object** | Configurations for the TOTP factors (channel) created under this Service. |  [optional] |
|**ttsName** | **String** | The name of an alternative text-to-speech service to use in phone calls. Applies only to TTS languages. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**verifyEventSubscriptionEnabled** | **Boolean** | Whether to allow verifications from the service to reach the stream-events sinks if configured |  [optional] |



