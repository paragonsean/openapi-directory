

# GoogleCloudIdentitytoolkitV2StartMfaEnrollmentRequest

Sends MFA enrollment verification SMS for a user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idToken** | **String** | Required. User&#39;s ID token. |  [optional] |
|**phoneEnrollmentInfo** | [**GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo**](GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo.md) |  |  [optional] |
|**tenantId** | **String** | The ID of the Identity Platform tenant that the user enrolling MFA belongs to. If not set, the user belongs to the default Identity Platform project. |  [optional] |
|**totpEnrollmentInfo** | **Object** | Mfa request info specific to TOTP auth for StartMfa. |  [optional] |



