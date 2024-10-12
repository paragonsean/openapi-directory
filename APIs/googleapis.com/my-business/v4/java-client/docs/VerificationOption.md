

# VerificationOption

The verification option represents how to verify the location (indicated by verification method) and where the verification will be sent to (indicated by display data).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressData** | [**AddressVerificationData**](AddressVerificationData.md) |  |  [optional] |
|**emailData** | [**EmailVerificationData**](EmailVerificationData.md) |  |  [optional] |
|**phoneData** | [**PhoneVerificationData**](PhoneVerificationData.md) |  |  [optional] |
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



