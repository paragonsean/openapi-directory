# SensitiveDataProtectionDlp.GooglePrivacyDlpV2KMapEstimationHistogramBucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketSize** | **String** | Number of records within these anonymity bounds. | [optional] 
**bucketValueCount** | **String** | Total number of distinct quasi-identifier tuple values in this bucket. | [optional] 
**bucketValues** | [**[GooglePrivacyDlpV2KMapEstimationQuasiIdValues]**](GooglePrivacyDlpV2KMapEstimationQuasiIdValues.md) | Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20. | [optional] 
**maxAnonymity** | **String** | Always greater than or equal to min_anonymity. | [optional] 
**minAnonymity** | **String** | Always positive. | [optional] 


