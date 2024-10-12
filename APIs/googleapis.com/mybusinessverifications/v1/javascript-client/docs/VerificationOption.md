# MyBusinessVerificationsApi.VerificationOption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressData** | [**AddressVerificationData**](AddressVerificationData.md) |  | [optional] 
**announcement** | **String** | Set only if the method is VETTED_PARTNER. | [optional] 
**emailData** | [**EmailVerificationData**](EmailVerificationData.md) |  | [optional] 
**phoneNumber** | **String** | Set only if the method is PHONE_CALL or SMS. Phone number that the PIN will be sent to. | [optional] 
**verificationMethod** | **String** | Method to verify the location. | [optional] 



## Enum: VerificationMethodEnum


* `VERIFICATION_METHOD_UNSPECIFIED` (value: `"VERIFICATION_METHOD_UNSPECIFIED"`)

* `ADDRESS` (value: `"ADDRESS"`)

* `EMAIL` (value: `"EMAIL"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `SMS` (value: `"SMS"`)

* `AUTO` (value: `"AUTO"`)

* `VETTED_PARTNER` (value: `"VETTED_PARTNER"`)




