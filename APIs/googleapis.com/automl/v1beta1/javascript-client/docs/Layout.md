# CloudAutoMlApi.Layout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingPoly** | [**BoundingPoly**](BoundingPoly.md) |  | [optional] 
**pageNumber** | **Number** | Page number of the text_segment in the original document, starts from 1. | [optional] 
**textSegment** | [**TextSegment**](TextSegment.md) |  | [optional] 
**textSegmentType** | **String** | The type of the text_segment in document. | [optional] 



## Enum: TextSegmentTypeEnum


* `TEXT_SEGMENT_TYPE_UNSPECIFIED` (value: `"TEXT_SEGMENT_TYPE_UNSPECIFIED"`)

* `TOKEN` (value: `"TOKEN"`)

* `PARAGRAPH` (value: `"PARAGRAPH"`)

* `FORM_FIELD` (value: `"FORM_FIELD"`)

* `FORM_FIELD_NAME` (value: `"FORM_FIELD_NAME"`)

* `FORM_FIELD_CONTENTS` (value: `"FORM_FIELD_CONTENTS"`)

* `TABLE` (value: `"TABLE"`)

* `TABLE_HEADER` (value: `"TABLE_HEADER"`)

* `TABLE_ROW` (value: `"TABLE_ROW"`)

* `TABLE_CELL` (value: `"TABLE_CELL"`)




