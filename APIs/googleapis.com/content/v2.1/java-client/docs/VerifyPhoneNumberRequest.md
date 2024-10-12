

# VerifyPhoneNumberRequest

Request message for the VerifyPhoneNumber method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneVerificationMethod** | [**PhoneVerificationMethodEnum**](#PhoneVerificationMethodEnum) | Verification method used to receive verification code. |  [optional] |
|**verificationCode** | **String** | The verification code that was sent to the phone number for validation. |  [optional] |
|**verificationId** | **String** | The verification ID returned by &#x60;requestphoneverification&#x60;. |  [optional] |



## Enum: PhoneVerificationMethodEnum

| Name | Value |
|---- | -----|
| PHONE_VERIFICATION_METHOD_UNSPECIFIED | &quot;PHONE_VERIFICATION_METHOD_UNSPECIFIED&quot; |
| SMS | &quot;SMS&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |



