# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | Optional. Confidence of detected Schema entity. Range &#x60;[0, 1]&#x60;. | [optional] 
**id** | **String** | Optional. Canonical id. This will be a unique value in the entity list for this document. | [optional] 
**mentionId** | **String** | Optional. Deprecated. Use &#x60;id&#x60; field instead. | [optional] 
**mentionText** | **String** | Optional. Text value of the entity e.g. &#x60;1600 Amphitheatre Pkwy&#x60;. | [optional] 
**normalizedValue** | [**GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue**](GoogleCloudDocumentaiV1beta3DocumentEntityNormalizedValue.md) |  | [optional] 
**pageAnchor** | [**GoogleCloudDocumentaiV1beta3DocumentPageAnchor**](GoogleCloudDocumentaiV1beta3DocumentPageAnchor.md) |  | [optional] 
**properties** | [**[GoogleCloudDocumentaiV1beta3DocumentEntity]**](GoogleCloudDocumentaiV1beta3DocumentEntity.md) | Optional. Entities can be nested to form a hierarchical data structure representing the content in the document. | [optional] 
**provenance** | [**GoogleCloudDocumentaiV1beta3DocumentProvenance**](GoogleCloudDocumentaiV1beta3DocumentProvenance.md) |  | [optional] 
**redacted** | **Boolean** | Optional. Whether the entity will be redacted for de-identification purposes. | [optional] 
**textAnchor** | [**GoogleCloudDocumentaiV1beta3DocumentTextAnchor**](GoogleCloudDocumentaiV1beta3DocumentTextAnchor.md) |  | [optional] 
**type** | **String** | Required. Entity type from a schema e.g. &#x60;Address&#x60;. | [optional] 


