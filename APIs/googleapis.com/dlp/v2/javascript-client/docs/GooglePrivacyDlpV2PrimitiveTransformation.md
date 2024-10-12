# SensitiveDataProtectionDlp.GooglePrivacyDlpV2PrimitiveTransformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketingConfig** | [**GooglePrivacyDlpV2BucketingConfig**](GooglePrivacyDlpV2BucketingConfig.md) |  | [optional] 
**characterMaskConfig** | [**GooglePrivacyDlpV2CharacterMaskConfig**](GooglePrivacyDlpV2CharacterMaskConfig.md) |  | [optional] 
**cryptoDeterministicConfig** | [**GooglePrivacyDlpV2CryptoDeterministicConfig**](GooglePrivacyDlpV2CryptoDeterministicConfig.md) |  | [optional] 
**cryptoHashConfig** | [**GooglePrivacyDlpV2CryptoHashConfig**](GooglePrivacyDlpV2CryptoHashConfig.md) |  | [optional] 
**cryptoReplaceFfxFpeConfig** | [**GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig**](GooglePrivacyDlpV2CryptoReplaceFfxFpeConfig.md) |  | [optional] 
**dateShiftConfig** | [**GooglePrivacyDlpV2DateShiftConfig**](GooglePrivacyDlpV2DateShiftConfig.md) |  | [optional] 
**fixedSizeBucketingConfig** | [**GooglePrivacyDlpV2FixedSizeBucketingConfig**](GooglePrivacyDlpV2FixedSizeBucketingConfig.md) |  | [optional] 
**redactConfig** | **Object** | Redact a given value. For example, if used with an &#x60;InfoTypeTransformation&#x60; transforming PHONE_NUMBER, and input &#39;My phone number is 206-555-0123&#39;, the output would be &#39;My phone number is &#39;. | [optional] 
**replaceConfig** | [**GooglePrivacyDlpV2ReplaceValueConfig**](GooglePrivacyDlpV2ReplaceValueConfig.md) |  | [optional] 
**replaceDictionaryConfig** | [**GooglePrivacyDlpV2ReplaceDictionaryConfig**](GooglePrivacyDlpV2ReplaceDictionaryConfig.md) |  | [optional] 
**replaceWithInfoTypeConfig** | **Object** | Replace each matching finding with the name of the info_type. | [optional] 
**timePartConfig** | [**GooglePrivacyDlpV2TimePartConfig**](GooglePrivacyDlpV2TimePartConfig.md) |  | [optional] 


