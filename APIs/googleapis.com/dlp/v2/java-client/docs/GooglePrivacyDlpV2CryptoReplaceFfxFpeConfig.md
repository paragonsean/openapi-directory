

# GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig

Replaces an identifier with a surrogate using Format Preserving Encryption (FPE) with the FFX mode of operation; however when used in the `ReidentifyContent` API method, it serves the opposite function by reversing the surrogate back into the original identifier. The identifier must be encoded as ASCII. For a given crypto key and context, the same identifier will be replaced with the same surrogate. Identifiers must be at least two characters long. In the case that the identifier is the empty string, it will be skipped. See https://cloud.google.com/sensitive-data-protection/docs/pseudonymization to learn more. Note: We recommend using CryptoDeterministicConfig for all use cases which do not require preserving the input alphabet space and size, plus warrant referential integrity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commonAlphabet** | [**CommonAlphabetEnum**](#CommonAlphabetEnum) | Common alphabets. |  [optional] |
|**context** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  |  [optional] |
|**cryptoKey** | [**GooglePrivacyDlpV2CryptoKey**](GooglePrivacyDlpV2CryptoKey.md) |  |  [optional] |
|**customAlphabet** | **String** | This is supported by mapping these to the alphanumeric characters that the FFX mode natively supports. This happens before/after encryption/decryption. Each character listed must appear only once. Number of characters must be in the range [2, 95]. This must be encoded as ASCII. The order of characters does not matter. The full list of allowed characters is: 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ~&#x60;!@#$%^&amp;*()_-+&#x3D;{[}]|\\:;\&quot;&#39;&lt;,&gt;.?/ |  [optional] |
|**radix** | **Integer** | The native way to select the alphabet. Must be in the range [2, 95]. |  [optional] |
|**surrogateInfoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  |  [optional] |



## Enum: CommonAlphabetEnum

| Name | Value |
|---- | -----|
| FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED | &quot;FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED&quot; |
| NUMERIC | &quot;NUMERIC&quot; |
| HEXADECIMAL | &quot;HEXADECIMAL&quot; |
| UPPER_CASE_ALPHA_NUMERIC | &quot;UPPER_CASE_ALPHA_NUMERIC&quot; |
| ALPHA_NUMERIC | &quot;ALPHA_NUMERIC&quot; |



