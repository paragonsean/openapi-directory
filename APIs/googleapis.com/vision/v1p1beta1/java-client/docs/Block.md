

# Block

Logical element on the page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockType** | [**BlockTypeEnum**](#BlockTypeEnum) | Detected block type (text, image etc) for this block. |  [optional] |
|**boundingBox** | [**BoundingPoly**](BoundingPoly.md) |  |  [optional] |
|**confidence** | **Float** | Confidence of the OCR results on the block. Range [0, 1]. |  [optional] |
|**paragraphs** | [**List&lt;Paragraph&gt;**](Paragraph.md) | List of paragraphs in this block (if this blocks is of type text). |  [optional] |
|**property** | [**TextProperty**](TextProperty.md) |  |  [optional] |



## Enum: BlockTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| TEXT | &quot;TEXT&quot; |
| TABLE | &quot;TABLE&quot; |
| PICTURE | &quot;PICTURE&quot; |
| RULER | &quot;RULER&quot; |
| BARCODE | &quot;BARCODE&quot; |



