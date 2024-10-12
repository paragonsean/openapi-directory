

# GooglePrivacyDlpV2TransformationSummary

Summary of a single transformation. Only one of 'transformation', 'field_transformation', or 'record_suppress' will be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**GooglePrivacyDlpV2FieldId**](GooglePrivacyDlpV2FieldId.md) |  |  [optional] |
|**fieldTransformations** | [**List&lt;GooglePrivacyDlpV2FieldTransformation&gt;**](GooglePrivacyDlpV2FieldTransformation.md) | The field transformation that was applied. If multiple field transformations are requested for a single field, this list will contain all of them; otherwise, only one is supplied. |  [optional] |
|**infoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  |  [optional] |
|**recordSuppress** | [**GooglePrivacyDlpV2RecordSuppression**](GooglePrivacyDlpV2RecordSuppression.md) |  |  [optional] |
|**results** | [**List&lt;GooglePrivacyDlpV2SummaryResult&gt;**](GooglePrivacyDlpV2SummaryResult.md) | Collection of all transformations that took place or had an error. |  [optional] |
|**transformation** | [**GooglePrivacyDlpV2PrimitiveTransformation**](GooglePrivacyDlpV2PrimitiveTransformation.md) |  |  [optional] |
|**transformedBytes** | **String** | Total size in bytes that were transformed in some way. |  [optional] |



