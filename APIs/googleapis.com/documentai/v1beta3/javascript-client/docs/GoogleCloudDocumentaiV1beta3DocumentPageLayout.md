# CloudDocumentAiApi.GoogleCloudDocumentaiV1beta3DocumentPageLayout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingPoly** | [**GoogleCloudDocumentaiV1beta3BoundingPoly**](GoogleCloudDocumentaiV1beta3BoundingPoly.md) |  | [optional] 
**confidence** | **Number** | Confidence of the current Layout within context of the object this layout is for. e.g. confidence can be for a single token, a table, a visual element, etc. depending on context. Range &#x60;[0, 1]&#x60;. | [optional] 
**orientation** | **String** | Detected orientation for the Layout. | [optional] 
**textAnchor** | [**GoogleCloudDocumentaiV1beta3DocumentTextAnchor**](GoogleCloudDocumentaiV1beta3DocumentTextAnchor.md) |  | [optional] 



## Enum: OrientationEnum


* `ORIENTATION_UNSPECIFIED` (value: `"ORIENTATION_UNSPECIFIED"`)

* `PAGE_UP` (value: `"PAGE_UP"`)

* `PAGE_RIGHT` (value: `"PAGE_RIGHT"`)

* `PAGE_DOWN` (value: `"PAGE_DOWN"`)

* `PAGE_LEFT` (value: `"PAGE_LEFT"`)




