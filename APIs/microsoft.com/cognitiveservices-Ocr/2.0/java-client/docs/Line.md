

# Line

An object representing a recognized text line.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingBox** | **List&lt;BigDecimal&gt;** | Quadrangle bounding box, with coordinates in original image. The eight numbers represent the four points (x-coordinate, y-coordinate from the left-top corner of the image) of the detected rectangle from the left-top corner in the clockwise direction. For images, coordinates are in pixels. For PDF, coordinates are in inches. |  [optional] |
|**text** | **String** | The text content of the line. |  [optional] |
|**words** | [**List&lt;Word&gt;**](Word.md) | List of words in the text line. |  [optional] |



