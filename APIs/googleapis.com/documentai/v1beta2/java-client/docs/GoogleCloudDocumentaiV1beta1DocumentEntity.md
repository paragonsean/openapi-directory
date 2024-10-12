

# GoogleCloudDocumentaiV1beta1DocumentEntity

An entity that could be a phrase in the text or a property that belongs to the document. It is a known entity type, such as a person, an organization, or location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **Float** | Optional. Confidence of detected Schema entity. Range &#x60;[0, 1]&#x60;. |  [optional] |
|**id** | **String** | Optional. Canonical id. This will be a unique value in the entity list for this document. |  [optional] |
|**mentionId** | **String** | Optional. Deprecated. Use &#x60;id&#x60; field instead. |  [optional] |
|**mentionText** | **String** | Optional. Text value of the entity e.g. &#x60;1600 Amphitheatre Pkwy&#x60;. |  [optional] |
|**normalizedValue** | [**GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue**](GoogleCloudDocumentaiV1beta1DocumentEntityNormalizedValue.md) |  |  [optional] |
|**pageAnchor** | [**GoogleCloudDocumentaiV1beta1DocumentPageAnchor**](GoogleCloudDocumentaiV1beta1DocumentPageAnchor.md) |  |  [optional] |
|**properties** | [**List&lt;GoogleCloudDocumentaiV1beta1DocumentEntity&gt;**](GoogleCloudDocumentaiV1beta1DocumentEntity.md) | Optional. Entities can be nested to form a hierarchical data structure representing the content in the document. |  [optional] |
|**provenance** | [**GoogleCloudDocumentaiV1beta1DocumentProvenance**](GoogleCloudDocumentaiV1beta1DocumentProvenance.md) |  |  [optional] |
|**redacted** | **Boolean** | Optional. Whether the entity will be redacted for de-identification purposes. |  [optional] |
|**textAnchor** | [**GoogleCloudDocumentaiV1beta1DocumentTextAnchor**](GoogleCloudDocumentaiV1beta1DocumentTextAnchor.md) |  |  [optional] |
|**type** | **String** | Required. Entity type from a schema e.g. &#x60;Address&#x60;. |  [optional] |



