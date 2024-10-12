

# GoogleCloudDocumentaiV1beta2DocumentPageLayout

Visual element describing a layout unit on a page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingPoly** | [**GoogleCloudDocumentaiV1beta2BoundingPoly**](GoogleCloudDocumentaiV1beta2BoundingPoly.md) |  |  [optional] |
|**confidence** | **Float** | Confidence of the current Layout within context of the object this layout is for. e.g. confidence can be for a single token, a table, a visual element, etc. depending on context. Range &#x60;[0, 1]&#x60;. |  [optional] |
|**orientation** | [**OrientationEnum**](#OrientationEnum) | Detected orientation for the Layout. |  [optional] |
|**textAnchor** | [**GoogleCloudDocumentaiV1beta2DocumentTextAnchor**](GoogleCloudDocumentaiV1beta2DocumentTextAnchor.md) |  |  [optional] |



## Enum: OrientationEnum

| Name | Value |
|---- | -----|
| ORIENTATION_UNSPECIFIED | &quot;ORIENTATION_UNSPECIFIED&quot; |
| PAGE_UP | &quot;PAGE_UP&quot; |
| PAGE_RIGHT | &quot;PAGE_RIGHT&quot; |
| PAGE_DOWN | &quot;PAGE_DOWN&quot; |
| PAGE_LEFT | &quot;PAGE_LEFT&quot; |



