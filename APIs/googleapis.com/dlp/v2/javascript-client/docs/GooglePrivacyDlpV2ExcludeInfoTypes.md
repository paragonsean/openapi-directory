# SensitiveDataProtectionDlp.GooglePrivacyDlpV2ExcludeInfoTypes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infoTypes** | [**[GooglePrivacyDlpV2InfoType]**](GooglePrivacyDlpV2InfoType.md) | InfoType list in ExclusionRule rule drops a finding when it overlaps or contained within with a finding of an infoType from this list. For example, for &#x60;InspectionRuleSet.info_types&#x60; containing \&quot;PHONE_NUMBER\&quot;&#x60; and &#x60;exclusion_rule&#x60; containing &#x60;exclude_info_types.info_types&#x60; with \&quot;EMAIL_ADDRESS\&quot; the phone number findings are dropped if they overlap with EMAIL_ADDRESS finding. That leads to \&quot;555-222-2222@example.org\&quot; to generate only a single finding, namely email address. | [optional] 


