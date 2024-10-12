# CloudVisionApi.GoogleCloudVisionV1p1beta1Block

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockType** | **String** | Detected block type (text, image etc) for this block. | [optional] 
**boundingBox** | [**GoogleCloudVisionV1p1beta1BoundingPoly**](GoogleCloudVisionV1p1beta1BoundingPoly.md) |  | [optional] 
**confidence** | **Number** | Confidence of the OCR results on the block. Range [0, 1]. | [optional] 
**paragraphs** | [**[GoogleCloudVisionV1p1beta1Paragraph]**](GoogleCloudVisionV1p1beta1Paragraph.md) | List of paragraphs in this block (if this blocks is of type text). | [optional] 
**property** | [**GoogleCloudVisionV1p1beta1TextAnnotationTextProperty**](GoogleCloudVisionV1p1beta1TextAnnotationTextProperty.md) |  | [optional] 



## Enum: BlockTypeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `TEXT` (value: `"TEXT"`)

* `TABLE` (value: `"TABLE"`)

* `PICTURE` (value: `"PICTURE"`)

* `RULER` (value: `"RULER"`)

* `BARCODE` (value: `"BARCODE"`)




