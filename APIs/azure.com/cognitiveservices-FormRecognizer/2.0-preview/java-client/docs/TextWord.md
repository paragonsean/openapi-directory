

# TextWord

An object representing a word.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | **List&lt;BigDecimal&gt;** | Quadrangle bounding box, with coordinates specified relative to the top-left of the original image. The eight numbers represent the four points, clockwise from the top-left corner relative to the text orientation. For image, the (x, y) coordinates are measured in pixels. For PDF, the (x, y) coordinates are measured in inches. |  |
|**confidence** | **BigDecimal** | Confidence value. |  [optional] |
|**text** | **String** | The text content of the word. |  |



