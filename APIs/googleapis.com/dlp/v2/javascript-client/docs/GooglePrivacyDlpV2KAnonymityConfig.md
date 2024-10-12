# SensitiveDataProtectionDlp.GooglePrivacyDlpV2KAnonymityConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityId** | [**GooglePrivacyDlpV2EntityId**](GooglePrivacyDlpV2EntityId.md) |  | [optional] 
**quasiIds** | [**[GooglePrivacyDlpV2FieldId]**](GooglePrivacyDlpV2FieldId.md) | Set of fields to compute k-anonymity over. When multiple fields are specified, they are considered a single composite key. Structs and repeated data types are not supported; however, nested fields are supported so long as they are not structs themselves or nested within a repeated field. | [optional] 


