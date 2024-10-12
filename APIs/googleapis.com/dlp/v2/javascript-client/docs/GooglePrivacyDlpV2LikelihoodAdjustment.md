# SensitiveDataProtectionDlp.GooglePrivacyDlpV2LikelihoodAdjustment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixedLikelihood** | **String** | Set the likelihood of a finding to a fixed value. | [optional] 
**relativeLikelihood** | **Number** | Increase or decrease the likelihood by the specified number of levels. For example, if a finding would be &#x60;POSSIBLE&#x60; without the detection rule and &#x60;relative_likelihood&#x60; is 1, then it is upgraded to &#x60;LIKELY&#x60;, while a value of -1 would downgrade it to &#x60;UNLIKELY&#x60;. Likelihood may never drop below &#x60;VERY_UNLIKELY&#x60; or exceed &#x60;VERY_LIKELY&#x60;, so applying an adjustment of 1 followed by an adjustment of -1 when base likelihood is &#x60;VERY_LIKELY&#x60; will result in a final likelihood of &#x60;LIKELY&#x60;. | [optional] 



## Enum: FixedLikelihoodEnum


* `LIKELIHOOD_UNSPECIFIED` (value: `"LIKELIHOOD_UNSPECIFIED"`)

* `VERY_UNLIKELY` (value: `"VERY_UNLIKELY"`)

* `UNLIKELY` (value: `"UNLIKELY"`)

* `POSSIBLE` (value: `"POSSIBLE"`)

* `LIKELY` (value: `"LIKELY"`)

* `VERY_LIKELY` (value: `"VERY_LIKELY"`)




