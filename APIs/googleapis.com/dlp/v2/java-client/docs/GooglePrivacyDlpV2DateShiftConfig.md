

# GooglePrivacyDlpV2DateShiftConfig

Shifts dates by random number of days, with option to be consistent for the same context. See https://cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting to learn more.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  |  [optional] |
|**cryptoKey** | [**GooglePrivacyDlpV2CryptoKey**](GooglePrivacyDlpV2CryptoKey.md) |  |  [optional] |
|**lowerBoundDays** | **Integer** | Required. For example, -5 means shift date to at most 5 days back in the past. |  [optional] |
|**upperBoundDays** | **Integer** | Required. Range of shift in days. Actual shift will be selected at random within this range (inclusive ends). Negative means shift to earlier in time. Must not be more than 365250 days (1000 years) each direction. For example, 3 means shift date to at most 3 days into the future. |  [optional] |



