# SensitiveDataProtectionDlp.GooglePrivacyDlpV2FixedSizeBucketingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketSize** | **Number** | Required. Size of each bucket (except for minimum and maximum buckets). So if &#x60;lower_bound&#x60; &#x3D; 10, &#x60;upper_bound&#x60; &#x3D; 89, and &#x60;bucket_size&#x60; &#x3D; 10, then the following buckets would be used: -10, 10-20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80, 80-89, 89+. Precision up to 2 decimals works. | [optional] 
**lowerBound** | [**GooglePrivacyDlpV2Value**](GooglePrivacyDlpV2Value.md) |  | [optional] 
**upperBound** | [**GooglePrivacyDlpV2Value**](GooglePrivacyDlpV2Value.md) |  | [optional] 


