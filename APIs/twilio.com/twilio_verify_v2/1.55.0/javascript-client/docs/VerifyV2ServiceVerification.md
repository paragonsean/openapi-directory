# TwilioVerify.VerifyV2ServiceVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Verification resource. | [optional] 
**amount** | **String** | The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] 
**channel** | [**VerificationEnumChannel**](VerificationEnumChannel.md) |  | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**lookup** | **Object** | Information about the phone number being verified. | [optional] 
**payee** | **String** | The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. | [optional] 
**sendCodeAttempts** | **[Object]** | An array of verification attempt objects containing the channel attempted and the channel-specific transaction SID. | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Verification resource. | [optional] 
**sna** | **Object** | The set of fields used for a silent network auth (&#x60;sna&#x60;) verification. Contains a single field with the URL to be invoked to verify the phone number. | [optional] 
**status** | **String** | The status of the verification. One of: &#x60;pending&#x60;, &#x60;approved&#x60;, or &#x60;canceled&#x60; | [optional] 
**to** | **String** | The phone number or [email](https://www.twilio.com/docs/verify/email) being verified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] 
**url** | **String** | The absolute URL of the Verification resource. | [optional] 
**valid** | **Boolean** | Use \&quot;status\&quot; instead. Legacy property indicating whether the verification was successful. | [optional] 


