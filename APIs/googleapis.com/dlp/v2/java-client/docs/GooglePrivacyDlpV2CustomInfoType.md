

# GooglePrivacyDlpV2CustomInfoType

Custom information type provided by the user. Used to find domain-specific sensitive information configurable to the data in question.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detectionRules** | [**List&lt;GooglePrivacyDlpV2DetectionRule&gt;**](GooglePrivacyDlpV2DetectionRule.md) | Set of detection rules to apply to all findings of this CustomInfoType. Rules are applied in order that they are specified. Not supported for the &#x60;surrogate_type&#x60; CustomInfoType. |  [optional] |
|**dictionary** | [**GooglePrivacyDlpV2Dictionary**](GooglePrivacyDlpV2Dictionary.md) |  |  [optional] |
|**exclusionType** | [**ExclusionTypeEnum**](#ExclusionTypeEnum) | If set to EXCLUSION_TYPE_EXCLUDE this infoType will not cause a finding to be returned. It still can be used for rules matching. |  [optional] |
|**infoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  |  [optional] |
|**likelihood** | [**LikelihoodEnum**](#LikelihoodEnum) | Likelihood to return for this CustomInfoType. This base value can be altered by a detection rule if the finding meets the criteria specified by the rule. Defaults to &#x60;VERY_LIKELY&#x60; if not specified. |  [optional] |
|**regex** | [**GooglePrivacyDlpV2Regex**](GooglePrivacyDlpV2Regex.md) |  |  [optional] |
|**sensitivityScore** | [**GooglePrivacyDlpV2SensitivityScore**](GooglePrivacyDlpV2SensitivityScore.md) |  |  [optional] |
|**storedType** | [**GooglePrivacyDlpV2StoredType**](GooglePrivacyDlpV2StoredType.md) |  |  [optional] |
|**surrogateType** | **Object** | Message for detecting output from deidentification transformations such as [&#x60;CryptoReplaceFfxFpeConfig&#x60;](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#cryptoreplaceffxfpeconfig). These types of transformations are those that perform pseudonymization, thereby producing a \&quot;surrogate\&quot; as output. This should be used in conjunction with a field on the transformation such as &#x60;surrogate_info_type&#x60;. This CustomInfoType does not support the use of &#x60;detection_rules&#x60;. |  [optional] |



## Enum: ExclusionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;EXCLUSION_TYPE_UNSPECIFIED&quot; |
| EXCLUDE | &quot;EXCLUSION_TYPE_EXCLUDE&quot; |



## Enum: LikelihoodEnum

| Name | Value |
|---- | -----|
| LIKELIHOOD_UNSPECIFIED | &quot;LIKELIHOOD_UNSPECIFIED&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



