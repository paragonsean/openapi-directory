

# RotatingBarcodeTotpDetails

Configuration for the time-based OTP substitutions. See https://tools.ietf.org/html/rfc6238

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | The TOTP algorithm used to generate the OTP. |  [optional] |
|**parameters** | [**List&lt;RotatingBarcodeTotpDetailsTotpParameters&gt;**](RotatingBarcodeTotpDetailsTotpParameters.md) | The TOTP parameters for each of the {totp_value_*} substitutions. The TotpParameters at index n is used for the {totp_value_n} substitution. |  [optional] |
|**periodMillis** | **String** | The time interval used for the TOTP value generation, in milliseconds. |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| ALGORITHM_UNSPECIFIED | &quot;TOTP_ALGORITHM_UNSPECIFIED&quot; |
| SHA1 | &quot;TOTP_SHA1&quot; |



