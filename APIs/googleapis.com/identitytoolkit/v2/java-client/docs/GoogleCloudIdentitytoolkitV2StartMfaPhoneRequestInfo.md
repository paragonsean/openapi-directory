

# GoogleCloudIdentitytoolkitV2StartMfaPhoneRequestInfo

App Verification info for a StartMfa request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoRetrievalInfo** | [**GoogleCloudIdentitytoolkitV2AutoRetrievalInfo**](GoogleCloudIdentitytoolkitV2AutoRetrievalInfo.md) |  |  [optional] |
|**iosReceipt** | **String** | iOS only. Receipt of successful app token validation with APNS. |  [optional] |
|**iosSecret** | **String** | iOS only. Secret delivered to iOS app via APNS. |  [optional] |
|**phoneNumber** | **String** | Required for enrollment. Phone number to be enrolled as MFA. |  [optional] |
|**playIntegrityToken** | **String** | Android only. Used to assert application identity in place of a recaptcha token (or safety net token). A Play Integrity Token can be generated via the [PlayIntegrity API] (https://developer.android.com/google/play/integrity) with applying SHA256 to the &#x60;phone_number&#x60; field as the nonce. |  [optional] |
|**recaptchaToken** | **String** | Web only. Recaptcha solution. |  [optional] |
|**safetyNetToken** | **String** | Android only. Used to assert application identity in place of a recaptcha token. A SafetyNet Token can be generated via the [SafetyNet Android Attestation API](https://developer.android.com/training/safetynet/attestation.html), with the Base64 encoding of the &#x60;phone_number&#x60; field as the nonce. |  [optional] |



