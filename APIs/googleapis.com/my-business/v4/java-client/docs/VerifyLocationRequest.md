

# VerifyLocationRequest

Request message for Verifications.VerifyLocation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressInput** | [**AddressInput**](AddressInput.md) |  |  [optional] |
|**context** | [**ServiceBusinessContext**](ServiceBusinessContext.md) |  |  [optional] |
|**emailInput** | [**EmailInput**](EmailInput.md) |  |  [optional] |
|**languageCode** | **String** | The BCP 47 language code representing the language that is to be used for the verification process. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | Verification method. |  [optional] |
|**phoneInput** | [**PhoneInput**](PhoneInput.md) |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| VERIFICATION_METHOD_UNSPECIFIED | &quot;VERIFICATION_METHOD_UNSPECIFIED&quot; |
| ADDRESS | &quot;ADDRESS&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| SMS | &quot;SMS&quot; |
| AUTO | &quot;AUTO&quot; |



