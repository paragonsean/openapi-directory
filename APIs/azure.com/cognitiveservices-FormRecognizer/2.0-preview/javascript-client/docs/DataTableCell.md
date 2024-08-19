# FormRecognizerClient.DataTableCell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boundingBox** | **[Number]** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. | 
**columnIndex** | **Number** | Column index of the cell. | 
**columnSpan** | **Number** | Number of columns spanned by this cell. | [optional] 
**confidence** | **Number** | Confidence value. | 
**elements** | **[String]** | When includeTextDetails is set to true, a list of references to the text elements constituting this table cell. | [optional] 
**isFooter** | **Boolean** | Is the current cell a footer cell? | [optional] [default to false]
**isHeader** | **Boolean** | Is the current cell a header cell? | [optional] [default to false]
**rowIndex** | **Number** | Row index of the cell. | 
**rowSpan** | **Number** | Number of rows spanned by this cell. | [optional] 
**text** | **String** | Text content of the cell. | 


