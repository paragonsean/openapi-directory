

# TextLine

An object representing an extracted text line.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | **List&lt;BigDecimal&gt;** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. |  |
|**language** | **Language** |  |  [optional] |
|**text** | **String** | The text content of the line. |  |
|**words** | [**List&lt;TextWord&gt;**](TextWord.md) | List of words in the text line. |  |



