

# GoogleCloudIdentitytoolkitV2FinalizeMfaPhoneRequestInfo

Phone Verification info for a FinalizeMfa request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidVerificationProof** | **String** | Android only. Uses for \&quot;instant\&quot; phone number verification though GmsCore. |  [optional] |
|**code** | **String** | User-entered verification code. |  [optional] |
|**phoneNumber** | **String** | Required if Android verification proof is presented. |  [optional] |
|**sessionInfo** | **String** | An opaque string that represents the enrollment session. |  [optional] |



