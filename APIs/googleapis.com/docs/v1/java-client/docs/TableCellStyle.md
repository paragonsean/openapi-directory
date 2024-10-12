

# TableCellStyle

The style of a TableCell. Inherited table cell styles are represented as unset fields in this message. A table cell style can inherit from the table's style.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backgroundColor** | [**OptionalColor**](OptionalColor.md) |  |  [optional] |
|**borderBottom** | [**TableCellBorder**](TableCellBorder.md) |  |  [optional] |
|**borderLeft** | [**TableCellBorder**](TableCellBorder.md) |  |  [optional] |
|**borderRight** | [**TableCellBorder**](TableCellBorder.md) |  |  [optional] |
|**borderTop** | [**TableCellBorder**](TableCellBorder.md) |  |  [optional] |
|**columnSpan** | **Integer** | The column span of the cell. This property is read-only. |  [optional] |
|**contentAlignment** | [**ContentAlignmentEnum**](#ContentAlignmentEnum) | The alignment of the content in the table cell. The default alignment matches the alignment for newly created table cells in the Docs editor. |  [optional] |
|**paddingBottom** | [**Dimension**](Dimension.md) |  |  [optional] |
|**paddingLeft** | [**Dimension**](Dimension.md) |  |  [optional] |
|**paddingRight** | [**Dimension**](Dimension.md) |  |  [optional] |
|**paddingTop** | [**Dimension**](Dimension.md) |  |  [optional] |
|**rowSpan** | **Integer** | The row span of the cell. This property is read-only. |  [optional] |



## Enum: ContentAlignmentEnum

| Name | Value |
|---- | -----|
| CONTENT_ALIGNMENT_UNSPECIFIED | &quot;CONTENT_ALIGNMENT_UNSPECIFIED&quot; |
| CONTENT_ALIGNMENT_UNSUPPORTED | &quot;CONTENT_ALIGNMENT_UNSUPPORTED&quot; |
| TOP | &quot;TOP&quot; |
| MIDDLE | &quot;MIDDLE&quot; |
| BOTTOM | &quot;BOTTOM&quot; |



