

# DataTableCell

Information about the extracted cell in a table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | **List&lt;BigDecimal&gt;** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. |  |
|**columnIndex** | **Integer** | Column index of the cell. |  |
|**columnSpan** | **Integer** | Number of columns spanned by this cell. |  [optional] |
|**confidence** | **BigDecimal** | Confidence value. |  |
|**elements** | **List&lt;String&gt;** | When includeTextDetails is set to true, a list of references to the text elements constituting this table cell. |  [optional] |
|**isFooter** | **Boolean** | Is the current cell a footer cell? |  [optional] |
|**isHeader** | **Boolean** | Is the current cell a header cell? |  [optional] |
|**rowIndex** | **Integer** | Row index of the cell. |  |
|**rowSpan** | **Integer** | Number of rows spanned by this cell. |  [optional] |
|**text** | **String** | Text content of the cell. |  |



