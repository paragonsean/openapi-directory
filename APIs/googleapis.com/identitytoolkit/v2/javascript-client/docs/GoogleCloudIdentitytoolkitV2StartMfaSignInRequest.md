# IdentityToolkitApi.GoogleCloudIdentitytoolkitV2StartMfaSignInRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfaEnrollmentId** | **String** | Required. MFA enrollment id from the user&#39;s list of current MFA enrollments. | [optional] 
**mfaPendingCredential** | **String** | Required. Pending credential from first factor sign-in. | [optional] 
**phoneSignInInfo** | [**GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo**](GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo.md) |  | [optional] 
**tenantId** | **String** | The ID of the Identity Platform tenant the user is signing in to. If not set, the user will sign in to the default Identity Platform project. | [optional] 


