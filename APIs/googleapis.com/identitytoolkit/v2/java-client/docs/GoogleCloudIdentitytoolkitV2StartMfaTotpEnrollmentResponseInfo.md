

# GoogleCloudIdentitytoolkitV2StartMfaTotpEnrollmentResponseInfo

Mfa response info specific to TOTP auth for StartMfa.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**finalizeEnrollmentTime** | **String** | The time by which the enrollment must finish. |  [optional] |
|**hashingAlgorithm** | **String** | The hashing algorithm used to generate the verification code. |  [optional] |
|**periodSec** | **Integer** | Duration in seconds at which the verification code will change. |  [optional] |
|**sessionInfo** | **String** | An encoded string that represents the enrollment session. |  [optional] |
|**sharedSecretKey** | **String** | A base 32 encoded string that represents the shared TOTP secret. The base 32 encoding is the one specified by [RFC4648#section-6](https://datatracker.ietf.org/doc/html/rfc4648#section-6). (This is the same as the base 32 encoding from [RFC3548#section-5](https://datatracker.ietf.org/doc/html/rfc3548#section-5).) |  [optional] |
|**verificationCodeLength** | **Integer** | The length of the verification code that needs to be generated. |  [optional] |



