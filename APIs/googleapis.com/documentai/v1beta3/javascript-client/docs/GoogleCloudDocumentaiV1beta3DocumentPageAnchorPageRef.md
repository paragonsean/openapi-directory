# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentPageAnchorPageRef

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingPoly** | [**GoogleCloudDocumentaiV1beta3BoundingPoly**](GoogleCloudDocumentaiV1beta3BoundingPoly.md) |  | [optional] 
**confidence** | **Number** | Optional. Confidence of detected page element, if applicable. Range &#x60;[0, 1]&#x60;. | [optional] 
**layoutId** | **String** | Optional. Deprecated. Use PageRef.bounding_poly instead. | [optional] 
**layoutType** | **String** | Optional. The type of the layout element that is being referenced if any. | [optional] 
**page** | **String** | Required. Index into the Document.pages element, for example using &#x60;Document.pages&#x60; to locate the related page element. This field is skipped when its value is the default &#x60;0&#x60;. See https://developers.google.com/protocol-buffers/docs/proto3#json. | [optional] 



## Enum: LayoutTypeEnum


* `LAYOUT_TYPE_UNSPECIFIED` (value: `"LAYOUT_TYPE_UNSPECIFIED"`)

* `BLOCK` (value: `"BLOCK"`)

* `PARAGRAPH` (value: `"PARAGRAPH"`)

* `LINE` (value: `"LINE"`)

* `TOKEN` (value: `"TOKEN"`)

* `VISUAL_ELEMENT` (value: `"VISUAL_ELEMENT"`)

* `TABLE` (value: `"TABLE"`)

* `FORM_FIELD` (value: `"FORM_FIELD"`)




