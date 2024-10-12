# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta2DocumentEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | Optional. Confidence of detected Schema entity. Range &#x60;[0, 1]&#x60;. | [optional] 
**id** | **String** | Optional. Canonical id. This will be a unique value in the entity list for this document. | [optional] 
**mentionId** | **String** | Optional. Deprecated. Use &#x60;id&#x60; field instead. | [optional] 
**mentionText** | **String** | Optional. Text value of the entity e.g. &#x60;1600 Amphitheatre Pkwy&#x60;. | [optional] 
**normalizedValue** | [**GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue**](GoogleCloudDocumentaiV1beta2DocumentEntityNormalizedValue.md) |  | [optional] 
**pageAnchor** | [**GoogleCloudDocumentaiV1beta2DocumentPageAnchor**](GoogleCloudDocumentaiV1beta2DocumentPageAnchor.md) |  | [optional] 
**properties** | [**[GoogleCloudDocumentaiV1beta2DocumentEntity]**](GoogleCloudDocumentaiV1beta2DocumentEntity.md) | Optional. Entities can be nested to form a hierarchical data structure representing the content in the document. | [optional] 
**provenance** | [**GoogleCloudDocumentaiV1beta2DocumentProvenance**](GoogleCloudDocumentaiV1beta2DocumentProvenance.md) |  | [optional] 
**redacted** | **Boolean** | Optional. Whether the entity will be redacted for de-identification purposes. | [optional] 
**textAnchor** | [**GoogleCloudDocumentaiV1beta2DocumentTextAnchor**](GoogleCloudDocumentaiV1beta2DocumentTextAnchor.md) |  | [optional] 
**type** | **String** | Required. Entity type from a schema e.g. &#x60;Address&#x60;. | [optional] 


