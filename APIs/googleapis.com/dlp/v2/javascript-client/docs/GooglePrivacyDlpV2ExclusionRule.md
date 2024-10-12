# SensitiveDataProtectionDlp.GooglePrivacyDlpV2ExclusionRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dictionary** | [**GooglePrivacyDlpV2Dictionary**](GooglePrivacyDlpV2Dictionary.md) |  | [optional] 
**excludeByHotword** | [**GooglePrivacyDlpV2ExcludeByHotword**](GooglePrivacyDlpV2ExcludeByHotword.md) |  | [optional] 
**excludeInfoTypes** | [**GooglePrivacyDlpV2ExcludeInfoTypes**](GooglePrivacyDlpV2ExcludeInfoTypes.md) |  | [optional] 
**matchingType** | **String** | How the rule is applied, see MatchingType documentation for details. | [optional] 
**regex** | [**GooglePrivacyDlpV2Regex**](GooglePrivacyDlpV2Regex.md) |  | [optional] 



## Enum: MatchingTypeEnum


* `UNSPECIFIED` (value: `"MATCHING_TYPE_UNSPECIFIED"`)

* `FULL_MATCH` (value: `"MATCHING_TYPE_FULL_MATCH"`)

* `PARTIAL_MATCH` (value: `"MATCHING_TYPE_PARTIAL_MATCH"`)

* `INVERSE_MATCH` (value: `"MATCHING_TYPE_INVERSE_MATCH"`)




