

# GooglePrivacyDlpV2InfoTypeTransformations

A type of transformation that will scan unstructured text and apply various `PrimitiveTransformation`s to each finding, where the transformation is applied to only values that were identified as a specific info_type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transformations** | [**List&lt;GooglePrivacyDlpV2InfoTypeTransformation&gt;**](GooglePrivacyDlpV2InfoTypeTransformation.md) | Required. Transformation for each infoType. Cannot specify more than one for a given infoType. |  [optional] |



