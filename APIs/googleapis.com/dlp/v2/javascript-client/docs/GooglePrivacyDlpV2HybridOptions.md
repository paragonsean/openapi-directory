# SensitiveDataProtectionDlp.GooglePrivacyDlpV2HybridOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A short description of where the data is coming from. Will be stored once in the job. 256 max length. | [optional] 
**labels** | **{String: String}** | To organize findings, these labels will be added to each finding. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: &#x60;[a-z]([-a-z0-9]*[a-z0-9])?&#x60;. Label values must be between 0 and 63 characters long and must conform to the regular expression &#x60;([a-z]([-a-z0-9]*[a-z0-9])?)?&#x60;. No more than 10 labels can be associated with a given finding. Examples: * &#x60;\&quot;environment\&quot; : \&quot;production\&quot;&#x60; * &#x60;\&quot;pipeline\&quot; : \&quot;etl\&quot;&#x60; | [optional] 
**requiredFindingLabelKeys** | **[String]** | These are labels that each inspection request must include within their &#39;finding_labels&#39; map. Request may contain others, but any missing one of these will be rejected. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: &#x60;[a-z]([-a-z0-9]*[a-z0-9])?&#x60;. No more than 10 keys can be required. | [optional] 
**tableOptions** | [**GooglePrivacyDlpV2TableOptions**](GooglePrivacyDlpV2TableOptions.md) |  | [optional] 


