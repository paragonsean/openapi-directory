# SwissNextGenBankingApiFramework.ChallengeData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInformation** | **String** | Additional explanation for the PSU to explain e.g. fallback mechanism for the chosen SCA method. The TPP is obliged to show this to the PSU.  | [optional] 
**data** | **[String]** | A collection of strings as challenge data. | [optional] 
**image** | **Blob** | PNG data (max. 512 kilobyte) to be displayed to the PSU, Base64 encoding, cp. [RFC4648]. This attribute is used only, when PHOTO_OTP or CHIP_OTP is the selected SCA method.  | [optional] 
**imageLink** | **String** | A link where the ASPSP will provides the challenge image for the TPP. | [optional] 
**otpFormat** | **String** | The format type of the OTP to be typed in. The admitted values are \&quot;characters\&quot; or \&quot;integer\&quot;. | [optional] 
**otpMaxLength** | **Number** | The maximal length for the OTP to be typed in by the PSU. | [optional] 



## Enum: OtpFormatEnum


* `characters` (value: `"characters"`)

* `integer` (value: `"integer"`)




