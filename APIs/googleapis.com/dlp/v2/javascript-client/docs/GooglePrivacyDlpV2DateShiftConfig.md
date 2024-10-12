# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DateShiftConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  | [optional] 
**cryptoKey** | [**GooglePrivacyDlpV2CryptoKey**](GooglePrivacyDlpV2CryptoKey.md) |  | [optional] 
**lowerBoundDays** | **Number** | Required. For example, -5 means shift date to at most 5 days back in the past. | [optional] 
**upperBoundDays** | **Number** | Required. Range of shift in days. Actual shift will be selected at random within this range (inclusive ends). Negative means shift to earlier in time. Must not be more than 365250 days (1000 years) each direction. For example, 3 means shift date to at most 3 days into the future. | [optional] 


