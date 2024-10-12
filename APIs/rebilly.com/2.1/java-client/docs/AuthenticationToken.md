

# AuthenticationToken


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentialId** | **String** | The credential&#39;s ID. |  [optional] [readonly] |
|**mode** | [**ModeEnum**](#ModeEnum) | The token&#39;s generation mode. |  [optional] |
|**otpRequired** | **Boolean** | Should OTP be required to exchange this token. |  [optional] |
|**token** | **String** | The token identifier string. |  [optional] [readonly] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| PASSWORD | &quot;password&quot; |
| PASSWORDLESS | &quot;passwordless&quot; |



