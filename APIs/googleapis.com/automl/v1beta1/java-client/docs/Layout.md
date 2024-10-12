

# Layout

Describes the layout information of a text_segment in the document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingPoly** | [**BoundingPoly**](BoundingPoly.md) |  |  [optional] |
|**pageNumber** | **Integer** | Page number of the text_segment in the original document, starts from 1. |  [optional] |
|**textSegment** | [**TextSegment**](TextSegment.md) |  |  [optional] |
|**textSegmentType** | [**TextSegmentTypeEnum**](#TextSegmentTypeEnum) | The type of the text_segment in document. |  [optional] |



## Enum: TextSegmentTypeEnum

| Name | Value |
|---- | -----|
| TEXT_SEGMENT_TYPE_UNSPECIFIED | &quot;TEXT_SEGMENT_TYPE_UNSPECIFIED&quot; |
| TOKEN | &quot;TOKEN&quot; |
| PARAGRAPH | &quot;PARAGRAPH&quot; |
| FORM_FIELD | &quot;FORM_FIELD&quot; |
| FORM_FIELD_NAME | &quot;FORM_FIELD_NAME&quot; |
| FORM_FIELD_CONTENTS | &quot;FORM_FIELD_CONTENTS&quot; |
| TABLE | &quot;TABLE&quot; |
| TABLE_HEADER | &quot;TABLE_HEADER&quot; |
| TABLE_ROW | &quot;TABLE_ROW&quot; |
| TABLE_CELL | &quot;TABLE_CELL&quot; |



