# CloudVisionApi.Block

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockType** | **String** | Detected block type (text, image etc) for this block. | [optional] 
**boundingBox** | [**BoundingPoly**](BoundingPoly.md) |  | [optional] 
**confidence** | **Number** | Confidence of the OCR results on the block. Range [0, 1]. | [optional] 
**paragraphs** | [**[Paragraph]**](Paragraph.md) | List of paragraphs in this block (if this blocks is of type text). | [optional] 
**property** | [**TextProperty**](TextProperty.md) |  | [optional] 



## Enum: BlockTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `TEXT` (value: `"TEXT"`)

* `TABLE` (value: `"TABLE"`)

* `PICTURE` (value: `"PICTURE"`)

* `RULER` (value: `"RULER"`)

* `BARCODE` (value: `"BARCODE"`)




