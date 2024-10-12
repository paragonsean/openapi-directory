

# RequestCodeRequestBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cc** | **String** | Numerical country code for the phone number you are registering |  |
|**cert** | **String** | Base64-encoded Verified Name certificate |  |
|**method** | [**MethodEnum**](#MethodEnum) | Method of receiving your registration code |  |
|**phoneNumber** | **String** | Phone number you are registering, without the country code or plus symbol (+) |  |
|**pin** | **String** | Existing 6-digit PIN — This is only required when two-factor verification is enabled on this account. |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| SMS | &quot;sms&quot; |
| VOICE | &quot;voice&quot; |



