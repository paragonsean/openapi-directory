

# GooglePrivacyDlpV2RecordTransformations

A type of transformation that is applied over structured data such as a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldTransformations** | [**List&lt;GooglePrivacyDlpV2FieldTransformation&gt;**](GooglePrivacyDlpV2FieldTransformation.md) | Transform the record by applying various field transformations. |  [optional] |
|**recordSuppressions** | [**List&lt;GooglePrivacyDlpV2RecordSuppression&gt;**](GooglePrivacyDlpV2RecordSuppression.md) | Configuration defining which records get suppressed entirely. Records that match any suppression rule are omitted from the output. |  [optional] |



