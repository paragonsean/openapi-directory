

# GooglePrivacyDlpV2ExclusionRule

The rule that specifies conditions when findings of infoTypes specified in `InspectionRuleSet` are removed from results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dictionary** | [**GooglePrivacyDlpV2Dictionary**](GooglePrivacyDlpV2Dictionary.md) |  |  [optional] |
|**excludeByHotword** | [**GooglePrivacyDlpV2ExcludeByHotword**](GooglePrivacyDlpV2ExcludeByHotword.md) |  |  [optional] |
|**excludeInfoTypes** | [**GooglePrivacyDlpV2ExcludeInfoTypes**](GooglePrivacyDlpV2ExcludeInfoTypes.md) |  |  [optional] |
|**matchingType** | [**MatchingTypeEnum**](#MatchingTypeEnum) | How the rule is applied, see MatchingType documentation for details. |  [optional] |
|**regex** | [**GooglePrivacyDlpV2Regex**](GooglePrivacyDlpV2Regex.md) |  |  [optional] |



## Enum: MatchingTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MATCHING_TYPE_UNSPECIFIED&quot; |
| FULL_MATCH | &quot;MATCHING_TYPE_FULL_MATCH&quot; |
| PARTIAL_MATCH | &quot;MATCHING_TYPE_PARTIAL_MATCH&quot; |
| INVERSE_MATCH | &quot;MATCHING_TYPE_INVERSE_MATCH&quot; |



