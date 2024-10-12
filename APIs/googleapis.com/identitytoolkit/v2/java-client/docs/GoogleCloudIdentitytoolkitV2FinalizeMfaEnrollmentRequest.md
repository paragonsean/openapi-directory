

# GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentRequest

Finishes enrolling a second factor for the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Display name which is entered by users to distinguish between different second factors with same type or different type. |  [optional] |
|**idToken** | **String** | Required. ID token. |  [optional] |
|**phoneVerificationInfo** | [**GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo**](GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo.md) |  |  [optional] |
|**tenantId** | **String** | The ID of the Identity Platform tenant that the user enrolling MFA belongs to. If not set, the user belongs to the default Identity Platform project. |  [optional] |
|**totpVerificationInfo** | [**GoogleCloudIdentitytoolkitV2FinalizeMfaTotpEnrollmentRequestInfo**](GoogleCloudIdentitytoolkitV2FinalizeMfaTotpEnrollmentRequestInfo.md) |  |  [optional] |



