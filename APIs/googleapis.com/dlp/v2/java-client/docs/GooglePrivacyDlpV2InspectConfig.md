

# GooglePrivacyDlpV2InspectConfig

Configuration description of the scanning process. When used with redactContent only info_types and min_likelihood are currently used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentOptions** | [**List&lt;ContentOptionsEnum&gt;**](#List&lt;ContentOptionsEnum&gt;) | Deprecated and unused. |  [optional] |
|**customInfoTypes** | [**List&lt;GooglePrivacyDlpV2CustomInfoType&gt;**](GooglePrivacyDlpV2CustomInfoType.md) | CustomInfoTypes provided by the user. See https://cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes to learn more. |  [optional] |
|**excludeInfoTypes** | **Boolean** | When true, excludes type information of the findings. This is not used for data profiling. |  [optional] |
|**includeQuote** | **Boolean** | When true, a contextual quote from the data that triggered a finding is included in the response; see Finding.quote. This is not used for data profiling. |  [optional] |
|**infoTypes** | [**List&lt;GooglePrivacyDlpV2InfoType&gt;**](GooglePrivacyDlpV2InfoType.md) | Restricts what info_types to look for. The values must correspond to InfoType values returned by ListInfoTypes or listed at https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference. When no InfoTypes or CustomInfoTypes are specified in a request, the system may automatically choose a default list of detectors to run, which may change over time. If you need precise control and predictability as to what detectors are run you should specify specific InfoTypes listed in the reference, otherwise a default list will be used, which may change over time. |  [optional] |
|**limits** | [**GooglePrivacyDlpV2FindingLimits**](GooglePrivacyDlpV2FindingLimits.md) |  |  [optional] |
|**minLikelihood** | [**MinLikelihoodEnum**](#MinLikelihoodEnum) | Only returns findings equal to or above this threshold. The default is POSSIBLE. In general, the highest likelihood setting yields the fewest findings in results and the lowest chance of a false positive. For more information, see [Match likelihood](https://cloud.google.com/sensitive-data-protection/docs/likelihood). |  [optional] |
|**minLikelihoodPerInfoType** | [**List&lt;GooglePrivacyDlpV2InfoTypeLikelihood&gt;**](GooglePrivacyDlpV2InfoTypeLikelihood.md) | Minimum likelihood per infotype. For each infotype, a user can specify a minimum likelihood. The system only returns a finding if its likelihood is above this threshold. If this field is not set, the system uses the InspectConfig min_likelihood. |  [optional] |
|**ruleSet** | [**List&lt;GooglePrivacyDlpV2InspectionRuleSet&gt;**](GooglePrivacyDlpV2InspectionRuleSet.md) | Set of rules to apply to the findings for this InspectConfig. Exclusion rules, contained in the set are executed in the end, other rules are executed in the order they are specified for each info type. |  [optional] |



## Enum: List&lt;ContentOptionsEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CONTENT_UNSPECIFIED&quot; |
| TEXT | &quot;CONTENT_TEXT&quot; |
| IMAGE | &quot;CONTENT_IMAGE&quot; |



## Enum: MinLikelihoodEnum

| Name | Value |
|---- | -----|
| LIKELIHOOD_UNSPECIFIED | &quot;LIKELIHOOD_UNSPECIFIED&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



