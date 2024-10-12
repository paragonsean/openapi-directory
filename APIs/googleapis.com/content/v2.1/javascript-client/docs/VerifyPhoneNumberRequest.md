# ContentApiForShopping.VerifyPhoneNumberRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phoneVerificationMethod** | **String** | Verification method used to receive verification code. | [optional] 
**verificationCode** | **String** | The verification code that was sent to the phone number for validation. | [optional] 
**verificationId** | **String** | The verification ID returned by &#x60;requestphoneverification&#x60;. | [optional] 



## Enum: PhoneVerificationMethodEnum


* `PHONE_VERIFICATION_METHOD_UNSPECIFIED` (value: `"PHONE_VERIFICATION_METHOD_UNSPECIFIED"`)

* `SMS` (value: `"SMS"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)




