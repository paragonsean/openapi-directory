

# GooglePrivacyDlpV2FieldTransformation

The transformation to apply to the field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | [**GooglePrivacyDlpV2RecordCondition**](GooglePrivacyDlpV2RecordCondition.md) |  |  [optional] |
|**fields** | [**List&lt;GooglePrivacyDlpV2FieldId&gt;**](GooglePrivacyDlpV2FieldId.md) | Required. Input field(s) to apply the transformation to. When you have columns that reference their position within a list, omit the index from the FieldId. FieldId name matching ignores the index. For example, instead of \&quot;contact.nums[0].type\&quot;, use \&quot;contact.nums.type\&quot;. |  [optional] |
|**infoTypeTransformations** | [**GooglePrivacyDlpV2InfoTypeTransformations**](GooglePrivacyDlpV2InfoTypeTransformations.md) |  |  [optional] |
|**primitiveTransformation** | [**GooglePrivacyDlpV2PrimitiveTransformation**](GooglePrivacyDlpV2PrimitiveTransformation.md) |  |  [optional] |



