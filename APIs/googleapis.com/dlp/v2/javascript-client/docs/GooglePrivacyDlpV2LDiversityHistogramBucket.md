# SensitiveDataProtectionDlp.GooglePrivacyDlpV2LDiversityHistogramBucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketSize** | **String** | Total number of equivalence classes in this bucket. | [optional] 
**bucketValueCount** | **String** | Total number of distinct equivalence classes in this bucket. | [optional] 
**bucketValues** | [**[GooglePrivacyDlpV2LDiversityEquivalenceClass]**](GooglePrivacyDlpV2LDiversityEquivalenceClass.md) | Sample of equivalence classes in this bucket. The total number of classes returned per bucket is capped at 20. | [optional] 
**sensitiveValueFrequencyLowerBound** | **String** | Lower bound on the sensitive value frequencies of the equivalence classes in this bucket. | [optional] 
**sensitiveValueFrequencyUpperBound** | **String** | Upper bound on the sensitive value frequencies of the equivalence classes in this bucket. | [optional] 


