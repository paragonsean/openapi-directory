# RebillyRestApi.AuthenticationToken

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentialId** | **String** | The credential&#39;s ID. | [optional] [readonly] 
**mode** | **String** | The token&#39;s generation mode. | [optional] [default to &#39;password&#39;]
**otpRequired** | **Boolean** | Should OTP be required to exchange this token. | [optional] 
**token** | **String** | The token identifier string. | [optional] [readonly] 



## Enum: ModeEnum


* `password` (value: `"password"`)

* `passwordless` (value: `"passwordless"`)




