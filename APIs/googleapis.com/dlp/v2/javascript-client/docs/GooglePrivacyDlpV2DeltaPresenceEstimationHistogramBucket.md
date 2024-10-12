# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DeltaPresenceEstimationHistogramBucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketSize** | **String** | Number of records within these probability bounds. | [optional] 
**bucketValueCount** | **String** | Total number of distinct quasi-identifier tuple values in this bucket. | [optional] 
**bucketValues** | [**[GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues]**](GooglePrivacyDlpV2DeltaPresenceEstimationQuasiIdValues.md) | Sample of quasi-identifier tuple values in this bucket. The total number of classes returned per bucket is capped at 20. | [optional] 
**maxProbability** | **Number** | Always greater than or equal to min_probability. | [optional] 
**minProbability** | **Number** | Between 0 and 1. | [optional] 


