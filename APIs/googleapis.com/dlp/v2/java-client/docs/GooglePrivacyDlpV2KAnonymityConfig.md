

# GooglePrivacyDlpV2KAnonymityConfig

k-anonymity metric, used for analysis of reidentification risk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityId** | [**GooglePrivacyDlpV2EntityId**](GooglePrivacyDlpV2EntityId.md) |  |  [optional] |
|**quasiIds** | [**List&lt;GooglePrivacyDlpV2FieldId&gt;**](GooglePrivacyDlpV2FieldId.md) | Set of fields to compute k-anonymity over. When multiple fields are specified, they are considered a single composite key. Structs and repeated data types are not supported; however, nested fields are supported so long as they are not structs themselves or nested within a repeated field. |  [optional] |



