# SensitiveDataProtectionDlp.GooglePrivacyDlpV2InspectConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentOptions** | **[String]** | Deprecated and unused. | [optional] 
**customInfoTypes** | [**[GooglePrivacyDlpV2CustomInfoType]**](GooglePrivacyDlpV2CustomInfoType.md) | CustomInfoTypes provided by the user. See https://cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes to learn more. | [optional] 
**excludeInfoTypes** | **Boolean** | When true, excludes type information of the findings. This is not used for data profiling. | [optional] 
**includeQuote** | **Boolean** | When true, a contextual quote from the data that triggered a finding is included in the response; see Finding.quote. This is not used for data profiling. | [optional] 
**infoTypes** | [**[GooglePrivacyDlpV2InfoType]**](GooglePrivacyDlpV2InfoType.md) | Restricts what info_types to look for. The values must correspond to InfoType values returned by ListInfoTypes or listed at https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference. When no InfoTypes or CustomInfoTypes are specified in a request, the system may automatically choose a default list of detectors to run, which may change over time. If you need precise control and predictability as to what detectors are run you should specify specific InfoTypes listed in the reference, otherwise a default list will be used, which may change over time. | [optional] 
**limits** | [**GooglePrivacyDlpV2FindingLimits**](GooglePrivacyDlpV2FindingLimits.md) |  | [optional] 
**minLikelihood** | **String** | Only returns findings equal to or above this threshold. The default is POSSIBLE. In general, the highest likelihood setting yields the fewest findings in results and the lowest chance of a false positive. For more information, see [Match likelihood](https://cloud.google.com/sensitive-data-protection/docs/likelihood). | [optional] 
**minLikelihoodPerInfoType** | [**[GooglePrivacyDlpV2InfoTypeLikelihood]**](GooglePrivacyDlpV2InfoTypeLikelihood.md) | Minimum likelihood per infotype. For each infotype, a user can specify a minimum likelihood. The system only returns a finding if its likelihood is above this threshold. If this field is not set, the system uses the InspectConfig min_likelihood. | [optional] 
**ruleSet** | [**[GooglePrivacyDlpV2InspectionRuleSet]**](GooglePrivacyDlpV2InspectionRuleSet.md) | Set of rules to apply to the findings for this InspectConfig. Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type. | [optional] 



## Enum: [ContentOptionsEnum]


* `UNSPECIFIED` (value: `"CONTENT_UNSPECIFIED"`)

* `TEXT` (value: `"CONTENT_TEXT"`)

* `IMAGE` (value: `"CONTENT_IMAGE"`)





## Enum: MinLikelihoodEnum


* `LIKELIHOOD_UNSPECIFIED` (value: `"LIKELIHOOD_UNSPECIFIED"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)




