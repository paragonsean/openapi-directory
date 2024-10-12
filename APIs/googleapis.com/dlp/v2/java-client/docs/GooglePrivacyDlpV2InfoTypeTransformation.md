

# GooglePrivacyDlpV2InfoTypeTransformation

A transformation to apply to text that is identified as a specific info_type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**infoTypes** | [**List&lt;GooglePrivacyDlpV2InfoType&gt;**](GooglePrivacyDlpV2InfoType.md) | InfoTypes to apply the transformation to. An empty list will cause this transformation to apply to all findings that correspond to infoTypes that were requested in &#x60;InspectConfig&#x60;. |  [optional] |
|**primitiveTransformation** | [**GooglePrivacyDlpV2PrimitiveTransformation**](GooglePrivacyDlpV2PrimitiveTransformation.md) |  |  [optional] |



