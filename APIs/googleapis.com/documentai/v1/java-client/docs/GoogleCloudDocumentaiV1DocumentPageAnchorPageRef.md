

# GoogleCloudDocumentaiV1DocumentPageAnchorPageRef

Represents a weak reference to a page element within a document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingPoly** | [**GoogleCloudDocumentaiV1BoundingPoly**](GoogleCloudDocumentaiV1BoundingPoly.md) |  |  [optional] |
|**confidence** | **Float** | Optional. Confidence of detected page element, if applicable. Range &#x60;[0, 1]&#x60;. |  [optional] |
|**layoutId** | **String** | Optional. Deprecated. Use PageRef.bounding_poly instead. |  [optional] |
|**layoutType** | [**LayoutTypeEnum**](#LayoutTypeEnum) | Optional. The type of the layout element that is being referenced if any. |  [optional] |
|**page** | **String** | Required. Index into the Document.pages element, for example using &#x60;Document.pages&#x60; to locate the related page element. This field is skipped when its value is the default &#x60;0&#x60;. See https://developers.google.com/protocol-buffers/docs/proto3#json. |  [optional] |



## Enum: LayoutTypeEnum

| Name | Value |
|---- | -----|
| LAYOUT_TYPE_UNSPECIFIED | &quot;LAYOUT_TYPE_UNSPECIFIED&quot; |
| BLOCK | &quot;BLOCK&quot; |
| PARAGRAPH | &quot;PARAGRAPH&quot; |
| LINE | &quot;LINE&quot; |
| TOKEN | &quot;TOKEN&quot; |
| VISUAL_ELEMENT | &quot;VISUAL_ELEMENT&quot; |
| TABLE | &quot;TABLE&quot; |
| FORM_FIELD | &quot;FORM_FIELD&quot; |



