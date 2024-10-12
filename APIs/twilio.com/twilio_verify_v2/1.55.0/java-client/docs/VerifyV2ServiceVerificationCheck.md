

# VerifyV2ServiceVerificationCheck


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the VerificationCheck resource. |  [optional] |
|**amount** | **String** | The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. |  [optional] |
|**channel** | **VerificationCheckEnumChannel** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Verification Check resource was created. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Verification Check resource was last updated. |  [optional] |
|**payee** | **String** | The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the VerificationCheck resource. |  [optional] |
|**snaAttemptsErrorCodes** | **List&lt;Object&gt;** | List of error codes as a result of attempting a verification using the &#x60;sna&#x60; channel. The error codes are chronologically ordered, from the first attempt to the latest attempt. This will be an empty list if no errors occured or &#x60;null&#x60; if the last channel used wasn&#39;t &#x60;sna&#x60;. |  [optional] |
|**status** | **String** | The status of the verification. Can be: &#x60;pending&#x60;, &#x60;approved&#x60;, or &#x60;canceled&#x60;. |  [optional] |
|**to** | **String** | The phone number or [email](https://www.twilio.com/docs/verify/email) being verified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). |  [optional] |
|**valid** | **Boolean** | Use \&quot;status\&quot; instead. Legacy property indicating whether the verification was successful. |  [optional] |



