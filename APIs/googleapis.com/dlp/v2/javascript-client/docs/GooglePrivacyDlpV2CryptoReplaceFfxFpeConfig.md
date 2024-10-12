# SensitiveDataProtectionDlp.GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commonAlphabet** | **String** | Common alphabets. | [optional] 
**context** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  | [optional] 
**cryptoKey** | [**GooglePrivacyDlpV2CryptoKey**](GooglePrivacyDlpV2CryptoKey.md) |  | [optional] 
**customAlphabet** | **String** | This is supported by mapping these to the alphanumeric characters that the FFX mode natively supports. This happens before/after encryption/decryption. Each character listed must appear only once. Number of characters must be in the range [2, 95]. This must be encoded as ASCII. The order of characters does not matter. The full list of allowed characters is: 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ~&#x60;!@#$%^&amp;*()_-+&#x3D;{[}]|\\:;\&quot;&#39;&lt;,&gt;.?/ | [optional] 
**radix** | **Number** | The native way to select the alphabet. Must be in the range [2, 95]. | [optional] 
**surrogateInfoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  | [optional] 



## Enum: CommonAlphabetEnum


* `FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED` (value: `"FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED"`)

* `NUMERIC` (value: `"NUMERIC"`)

* `HEXADECIMAL` (value: `"HEXADECIMAL"`)

* `UPPER_CASE_ALPHA_NUMERIC` (value: `"UPPER_CASE_ALPHA_NUMERIC"`)

* `ALPHA_NUMERIC` (value: `"ALPHA_NUMERIC"`)




