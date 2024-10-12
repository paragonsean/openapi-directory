

# GoogleCloudIdentitytoolkitV2FinalizeMfaSignInRequest

Finalizes sign-in by verifying MFA challenge.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mfaEnrollmentId** | **String** | The MFA enrollment ID from the user&#39;s list of current MFA enrollments. |  [optional] |
|**mfaPendingCredential** | **String** | Required. Pending credential from first factor sign-in. |  [optional] |
|**phoneVerificationInfo** | [**GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo**](GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo.md) |  |  [optional] |
|**tenantId** | **String** | The ID of the Identity Platform tenant the user is signing in to. If not set, the user will sign in to the default Identity Platform project. |  [optional] |
|**totpVerificationInfo** | [**GoogleCloudIdentitytoolkitV2MfaTotpSignInRequestInfo**](GoogleCloudIdentitytoolkitV2MfaTotpSignInRequestInfo.md) |  |  [optional] |



