# SensitiveDataProtectionDlp.GooglePrivacyDlpV2FindingLimits

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxFindingsPerInfoType** | [**[GooglePrivacyDlpV2InfoTypeLimit]**](GooglePrivacyDlpV2InfoTypeLimit.md) | Configuration of findings limit given for specified infoTypes. | [optional] 
**maxFindingsPerItem** | **Number** | Max number of findings that are returned for each item scanned. When set within an InspectContentRequest, this field is ignored. This value isn&#39;t a hard limit. If the number of findings for an item reaches this limit, the inspection of that item ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns for the item can be multiple times higher than this value. | [optional] 
**maxFindingsPerRequest** | **Number** | Max number of findings that are returned per request or job. If you set this field in an InspectContentRequest, the resulting maximum value is the value that you set or 3,000, whichever is lower. This value isn&#39;t a hard limit. If an inspection reaches this limit, the inspection ends gradually, not abruptly. Therefore, the actual number of findings that Cloud DLP returns can be multiple times higher than this value. | [optional] 


