# GoogleMyBusinessApi.VerifyLocationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressInput** | [**AddressInput**](AddressInput.md) |  | [optional] 
**context** | [**ServiceBusinessContext**](ServiceBusinessContext.md) |  | [optional] 
**emailInput** | [**EmailInput**](EmailInput.md) |  | [optional] 
**languageCode** | **String** | The BCP 47 language code representing the language that is to be used for the verification process. | [optional] 
**method** | **String** | Verification method. | [optional] 
**phoneInput** | [**PhoneInput**](PhoneInput.md) |  | [optional] 



## Enum: MethodEnum


* `VERIFICATION_METHOD_UNSPECIFIED` (value: `"VERIFICATION_METHOD_UNSPECIFIED"`)

* `ADDRESS` (value: `"ADDRESS"`)

* `EMAIL` (value: `"EMAIL"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `SMS` (value: `"SMS"`)

* `AUTO` (value: `"AUTO"`)




