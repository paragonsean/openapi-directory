# GoogleWalletApi.RotatingBarcodeTotpDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | The TOTP algorithm used to generate the OTP. | [optional] 
**parameters** | [**[RotatingBarcodeTotpDetailsTotpParameters]**](RotatingBarcodeTotpDetailsTotpParameters.md) | The TOTP parameters for each of the {totp_value_*} substitutions. The TotpParameters at index n is used for the {totp_value_n} substitution. | [optional] 
**periodMillis** | **String** | The time interval used for the TOTP value generation, in milliseconds. | [optional] 



## Enum: AlgorithmEnum


* `ALGORITHM_UNSPECIFIED` (value: `"TOTP_ALGORITHM_UNSPECIFIED"`)

* `SHA1` (value: `"TOTP_SHA1"`)




