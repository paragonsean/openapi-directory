

# VerificationOption

The verification option represents how to verify the location (indicated by verification method) and where the verification will be sent to (indicated by display data).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressData** | [**AddressVerificationData**](AddressVerificationData.md) |  |  [optional] |
|**announcement** | **String** | Set only if the method is VETTED_PARTNER. |  [optional] |
|**emailData** | [**EmailVerificationData**](EmailVerificationData.md) |  |  [optional] |
|**phoneNumber** | **String** | Set only if the method is PHONE_CALL or SMS. Phone number that the PIN will be sent to. |  [optional] |
|**verificationMethod** | [**VerificationMethodEnum**](#VerificationMethodEnum) | Method to verify the location. |  [optional] |



## Enum: VerificationMethodEnum

| Name | Value |
|---- | -----|
| VERIFICATION_METHOD_UNSPECIFIED | &quot;VERIFICATION_METHOD_UNSPECIFIED&quot; |
| ADDRESS | &quot;ADDRESS&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| SMS | &quot;SMS&quot; |
| AUTO | &quot;AUTO&quot; |
| VETTED_PARTNER | &quot;VETTED_PARTNER&quot; |



